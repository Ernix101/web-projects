const student1 = {
    name: "Ernest",
    age: 21,
    university: "Kenyatta University",
    course: "Health Systems Management",
    skills: ['Domain knowledge', 'Python', 'Django', 'Javascript', 'Excel', 'DHIS2'],
}

// student1.skills.push("PostgreSQL")
// console.log(student1.skills)

function describeStudent(student) {
    return `${student.name} studies ${student.course} at ${student.university}`
}

// console.log(describeStudent(student1))

const anotherSkill = "Power BI"

function addSkill(student, newSkill) {
    student.skills.push(newSkill)
    return student.skills
}

// console.log(addSkill(student1, anotherSkill))

const upperSkills = student1.skills.map(skill => skill.toUpperCase())
// console.log(upperSkills)


sixCharactersOrMore = student1.skills.filter(skill => skill.length > 6)
// console.log(sixCharactersOrMore)

function listItems(array) {
    const ul = document.getElementById('skillList')
    ul.innerHTML = ''
    array.forEach(item => {
        const li = document.createElement('li')
        li.textContent = item
        ul.appendChild(li)
    });

    // document.body.appendChild(ul)
}
// listItems(student1.skills);


// Adding an input to create and push new skills
const skillForm = document.getElementById("skillForm")
const skillInput = document.getElementById("skillInput")



skillForm.addEventListener('submit', (e) => {
    e.preventDefault();

    const enteredSkill = skillInput.value
    if (enteredSkill.trim() === '') return
    addSkill(student1, enteredSkill);
    document.querySelector('ul').innerHTML = ''
    listItems(student1.skills);
});
