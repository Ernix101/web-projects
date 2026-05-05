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

console.log(addSkill(student1, anotherSkill))