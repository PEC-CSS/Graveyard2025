const pattern = [
    [1, 2, 3, 2, 3],
    [3, 1, 2, 1, 2],
    [2, 3, 1, 3, 1],
    [3, 2, 3, 1, 2],
    [2, 3, 2, 3, 1]
];

// Correctly add event listener without invoking the function
document.getElementById('btn').addEventListener('click', updateColours);

function updateColours() {
    // Get grid items
    const grids = document.querySelectorAll(".grid");

    // Get user-selected colors
    const color1 = document.getElementById('color1').value;
    const color2 = document.getElementById('color2').value;
    const color3 = document.getElementById('color3').value;

    // Apply colors based on the pattern
    grids.forEach((grid, index) => {
        const row = Math.floor(index / 5);
        const col = index % 5;
        const colorIndex = pattern[row][col];

        if (colorIndex === 1) {
            grid.style.backgroundColor = color1;
        } else if (colorIndex === 2) {
            grid.style.backgroundColor = color2;
        } else {
            grid.style.backgroundColor = color3;
        }
    });
}

// console.log(document.querySelectorAll("#grids"))

