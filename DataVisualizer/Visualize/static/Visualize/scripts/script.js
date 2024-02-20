

var table_results_json = JSON.parse('{{ table_results_json|escapejs }}');


const y_axis = table_results_json.map(item => item.fields.YAxis);
const x_axis = table_results_json.map(item => item.fields.XAxis);


// Create the chart
const ctx = document.getElementById('table_results_canvas').getContext('2d');
const chart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: x_axis,
        datasets: [{
            label: 'US GDP Per Capita (1971-2021)',
            data: y_axis,
            borderColor: 'rgb(75, 192, 192)',
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            fill: true
        }]
    },
    options: {
        scales: {
            x: {
                title: {
                    display: true,
                    text: 'yyyyyyyyyyyyyuuuuuuuuuxxxxxxx'
                }
            },
            y: {
                title: {
                    display: true,
                    text: 'yyyyyy'
                }
            }
        }
    }
});

var IsTableSelected = false;
var ugTableNames = {{ ug_table_names_ids_json| safe }};


const input = document.getElementById("combo");
const dropdown = document.getElementById("customDropdown");

const itemsList = ugTableNames;


itemsList.forEach(item => {
    const div = document.createElement("div");
    div.textContent = item.table_name;
    div.setAttribute("data-id", item.ug_table_id);
    div.onclick = function () {
        input.value = item.table_name;
        dropdown.style.display = "none";
        updateColumnsDropdown(item.ug_table_id);
    };
    dropdown.appendChild(div);
});





input.onfocus = function () {
    dropdown.style.display = "block";
    filterDropdown();
};

input.onblur = function () {
    setTimeout(() => {
        dropdown.style.display = "none";
    }, 150);
};

input.oninput = filterDropdown;

function filterDropdown() {
    const value = input.value.toLowerCase();
    const items = dropdown.children;
    for (let item of items) {
        if (item.textContent.toLowerCase().includes(value)) {
            item.style.display = "";
        } else {
            item.style.display = "none";
        }
    }
}





let comboText = document.getElementById("combo");

let y_Axis_DropdownInput = document.getElementById("y_Axis_Dropdown");
let y_AxisTextInput = document.getElementById("y_axis");

let x_Axis_DropdownInput = document.getElementById("x_Axis_Dropdown");  // x axis addition
let x_AxisTextInput = document.getElementById("x_axis");           // x axis addition




function updateColumnsDropdown(selectedTableId) {
    IsTableSelected = true;
    let columnsData = {{ columns_results_json| safe
}};

let columnsForSelectedTable = columnsData.filter(column => column.fields.ug_table_id == selectedTableId.toString());

y_Axis_DropdownInput.innerHTML = "";
x_Axis_DropdownInput.innerHTML = ""; // x axis addition

columnsForSelectedTable.forEach(column => {
    const div = document.createElement("div");
    div.textContent = column.fields.column_name; // Adjusted here
    div.onclick = function () {
        y_AxisTextInput.value = column.fields.column_name; // Adjusted here
        y_Axis_DropdownInput.style.display = "none";
    };
    y_Axis_DropdownInput.appendChild(div);
});






// x axis addition -------------->
columnsForSelectedTable.forEach(column => {
    const divx = document.createElement("div");
    divx.textContent = column.fields.column_name; // Adjusted here
    divx.onclick = function () {
        x_AxisTextInput.value = column.fields.column_name; // Adjusted here
        x_Axis_DropdownInput.style.display = "none";
    };
    x_Axis_DropdownInput.appendChild(divx);
});
}

// x axis addition -------------->




























y_AxisTextInput.addEventListener("focus", function () {
    y_Axis_DropdownInput.style.display = "block";
    if (IsTableSelected)
        updateColumnsDropdown(selectedTableId); // Show the dropdown on focus
});

y_AxisTextInput.addEventListener("input", function () {
    y_Axis_DropdownInput.style.display = "block";
    if (this.value === "") {
        if (IsTableSelected)
            updateColumnsDropdown(selectedTableId); // Show the dropdown when input is empty
    }
});

y_AxisTextInput.addEventListener('focus', function () {
    this.select();  // Selects the entire text content of the input
});

comboText.addEventListener('focus', function () {
    this.select();  // Selects the entire text content of the input
});


// x axis Input ----------------------------------------->


x_AxisTextInput.addEventListener("focus", function () {
    x_Axis_DropdownInput.style.display = "block";
    if (IsTableSelected)
        updateColumnsDropdown(selectedTableId); // Show the dropdown on focus
});

x_AxisTextInput.addEventListener("input", function () {
    x_Axis_DropdownInput.style.display = "block";
    if (this.value === "") {
        if (IsTableSelected)
            updateColumnsDropdown(selectedTableId); // Show the dropdown when input is empty
    }
});

x_AxisTextInput.addEventListener('focus', function () {
    this.select();  // Selects the entire text content of the input
});




















// x axis Input ----------------------------------------->









document.addEventListener("mousedown", function (event) {
    // Check if the clicked element is NOT the input box or any of its child elements
    if (y_AxisTextInput !== event.target && !y_AxisTextInput.contains(event.target)
        && y_Axis_DropdownInput !== event.target && !y_Axis_DropdownInput.contains(event.target)) {
        y_Axis_DropdownInput.style.display = "none";
    }

    if (x_AxisTextInput !== event.target && !x_AxisTextInput.contains(event.target)
        && x_Axis_DropdownInput !== event.target && !x_Axis_DropdownInput.contains(event.target)) {
        x_Axis_DropdownInput.style.display = "none";
    }


});


