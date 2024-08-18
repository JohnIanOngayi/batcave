#!/usr/bin/node

// Create interface for Student object
interface Student {
  firstName: string;
  lastName: string;
  age: number;
  location: string;
}

const student1: Student = {
  firstName: "John",
  lastName: "Doe",
  age: 25,
  location: "Kenya",
};
const student2: Student = {
  firstName: "Jane",
  lastName: "Blu",
  age: 21,
  location: "Kenya",
};
const studentsList: Student[] = [student1, student2];

document.addEventListener("DOMContentLoaded", () => {
  const table = document.createElement("table");
  const thead = document.createElement("thead");
  const tbody = document.createElement("tbody");

  // Create header row
  const headerRow = document.createElement("tr");
  ["First Name", "Location"].forEach((headerText) => {
    const header = document.createElement("th");
    header.textContent = headerText;
    headerRow.appendChild(header);
  });
  thead.appendChild(headerRow);

  // Append students to table body
  studentsList.forEach((student) => {
    const row = document.createElement("tr");

    const firstNameCell = document.createElement("td");
    firstNameCell.textContent = student.firstName;
    row.appendChild(firstNameCell);

    const locationCell = document.createElement("td");
    locationCell.textContent = student.location;
    row.appendChild(locationCell);

    tbody.appendChild(row);
  });

  // Assemble table
  table.appendChild(thead);
  table.appendChild(tbody);

  // Append table to body or a specific container
  document.body.appendChild(table); // Or use another container like document.getElementById('container').appendChild(table);
});
