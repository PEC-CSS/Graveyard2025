import tensorflow as tf
from keras import layers, Model
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.metrics import adjusted_rand_score
from skimage.metrics import structural_similarity as ssim

# Load MNIST dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train = x_train.astype('float32') / 255.
x_test = x_test.astype('float32') / 255.
x_train = x_train.reshape(-1, 784)  # Flatten images
x_test = x_test.reshape(-1, 784)  # Flatten images

# Function to add noise for Denoising Autoencoder
def add_noise(images, noise_factor=0.5):
    noisy = images + noise_factor * np.random.normal(loc=0.0, scale=1.0, size=images.shape)
    return np.clip(noisy, 0., 1.)

# Create noisy datasets
x_train_noisy = add_noise(x_train)
x_test_noisy = add_noise(x_test)

### Vanilla Autoencoder ###
class VanillaAutoencoder(Model):
    def __init__(self, latent_dim):
        super(VanillaAutoencoder, self).__init__()
        self.encoder = tf.keras.Sequential([
            layers.Dense(256, activation='relu'),
            layers.Dense(128, activation='relu'),
            layers.Dense(latent_dim, activation='relu')
        ])
        self.decoder = tf.keras.Sequential([
            layers.Dense(128, activation='relu'),
            layers.Dense(256, activation='relu'),
            layers.Dense(784, activation='sigmoid')
        ])
    
    def call(self, x):
        return self.decoder(self.encoder(x))

### Variational Autoencoder (VAE) ###
class VariationalAutoencoder(Model):
    def __init__(self, latent_dim):
        super(VariationalAutoencoder, self).__init__()
        self.latent_dim = latent_dim
        self.encoder = tf.keras.Sequential([
            layers.Dense(256, activation='relu'),
            layers.Dense(128, activation='relu'),
            layers.Dense(2 * latent_dim)  # Outputs mean and log variance
        ])
        self.decoder = tf.keras.Sequential([
            layers.Dense(128, activation='relu'),
            layers.Dense(256, activation='relu'),
            layers.Dense(784, activation='sigmoid')
        ])
    
    def sample(self, mean, logvar):
        eps = tf.random.normal(shape=tf.shape(mean))
        return mean + tf.exp(0.5 * logvar) * eps
    
    def call(self, x):
        encoded = self.encoder(x)
        mean, logvar = tf.split(encoded, 2, axis=1)
        z = self.sample(mean, logvar)
        reconstructed = self.decoder(z)
        kl_loss = -0.5 * tf.reduce_sum(1 + logvar - tf.square(mean) - tf.exp(logvar), axis=1)
        self.add_loss(tf.reduce_mean(kl_loss))  # Add KL divergence loss
        return reconstructed

### Denoising Autoencoder (inherits from Vanilla Autoencoder) ###
class DenoisingAutoencoder(VanillaAutoencoder):
    pass  # Uses the same architecture as Vanilla AE

latent_dim = 32

# Train Vanilla Autoencoder
vanilla_ae = VanillaAutoencoder(latent_dim)
vanilla_ae.compile(optimizer='adam', loss='mse')
vanilla_ae.fit(x_train, x_train, epochs=30, batch_size=256, validation_data=(x_test, x_test))

# Train Variational Autoencoder
vae = VariationalAutoencoder(latent_dim)
vae.compile(optimizer='adam')
vae.fit(x_train, x_train, epochs=30, batch_size=256, validation_data=(x_test, x_test))

# Train Denoising Autoencoder
denoising_ae = DenoisingAutoencoder(latent_dim)
denoising_ae.compile(optimizer='adam', loss='mse')
denoising_ae.fit(x_train_noisy, x_train, epochs=30, batch_size=256, validation_data=(x_test_noisy, x_test))

# Function to evaluate reconstruction quality
def evaluate_reconstruction(model, x_true, x_input=None):
    x_input = x_true if x_input is None else x_input
    reconstructed = model.predict(x_input)
    mse = tf.keras.losses.MSE(x_true, reconstructed).numpy().mean()
    ssim_scores = [ssim(x_true[i].reshape(28,28), reconstructed[i].reshape(28,28), data_range=1.0) 
                   for i in range(len(x_true))]
    return mse, np.mean(ssim_scores)

# Evaluate models
mse_vanilla, ssim_vanilla = evaluate_reconstruction(vanilla_ae, x_test)
mse_vae, ssim_vae = evaluate_reconstruction(vae, x_test)
mse_denoising, ssim_denoising = evaluate_reconstruction(denoising_ae, x_test, x_test_noisy)

# Print evaluation metrics
print(f"Vanilla AE - MSE: {mse_vanilla:.4f}, SSIM: {ssim_vanilla:.4f}")
print(f"VAE - MSE: {mse_vae:.4f}, SSIM: {ssim_vae:.4f}")
print(f"Denoising AE - MSE: {mse_denoising:.4f}, SSIM: {ssim_denoising:.4f}")

# Function to extract latent representations
def get_latent_representations(model, data):
    if isinstance(model, VariationalAutoencoder):
        latent = model.encoder(data)
        mean, _ = np.split(latent, 2, axis=1)  # Extract mean from (mean, logvar)
        return mean
    return model.encoder.predict(data)

latent_vanilla = get_latent_representations(vanilla_ae, x_test)
latent_vae = get_latent_representations(vae, x_test)
latent_dae = get_latent_representations(denoising_ae, x_test_noisy)

# Apply t-SNE for visualization
tsne = TSNE(n_components=2, random_state=42)
latent_vanilla_tsne = tsne.fit_transform(latent_vanilla)
latent_vae_tsne = tsne.fit_transform(latent_vae)
latent_dae_tsne = tsne.fit_transform(latent_dae)

# Function to plot t-SNE results
def plot_latent(latent, labels, title):
    plt.figure(figsize=(10,8))
    plt.scatter(latent[:,0], latent[:,1], c=labels, cmap='tab10', alpha=0.6)
    plt.colorbar()
    plt.title(title)
    plt.show()

# Plot latent spaces
plot_latent(latent_vanilla_tsne, y_test, 'Vanilla Autoencoder')
plot_latent(latent_vae_tsne, y_test, 'Variational Autoencoder')
plot_latent(latent_dae_tsne, y_test, 'Denoising Autoencoder')
