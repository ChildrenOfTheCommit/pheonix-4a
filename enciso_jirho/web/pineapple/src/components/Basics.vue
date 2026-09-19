<script setup lang="ts">
let student_age: number = 20;
const school_name: string = "CSU Carig";

console.log("Switch Case Test");
switch (student_age) {
  case 18:
    console.log("Freshman age");
    break;
  case 20:
    console.log("Junior age");
    break;
  case 22:
    console.log("Senior age");
    break;
  default:
    console.log("What did you put that triggered this default -_-");
    break;
}

if (student_age < 18) {
  console.log("Student is a minor.");
} else if (student_age >= 18 && student_age < 65) {
  console.log("Student is an adult.");
} else if (student_age > 100) {
  console.log("Why are you still alive?");
} else {
  console.log("Wow healthy living");
}

const num: number = 3;
for (let i: number = 1; i <= num; i++) {
  console.log(i);
}

interface Student {
  user_name: string;
  first_name: string;
  student_age: number;
  is_enrolled: boolean;
  gpa_score: number;
}

const current_student: Student = {
  user_name: "j_doe99",
  first_name: "John",
  student_age: student_age,
  is_enrolled: true,
  gpa_score: 3.8,
};
</script>

<template></template>

<style></style>
