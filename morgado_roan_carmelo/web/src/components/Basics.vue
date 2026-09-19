<script lang="ts">
let accounts = {
  username: "roanmorgado",
  password: "1234",
  displayName : "Melo"
}
console.log(accounts)

interface student {
  username : string
  password : string
  displayName : string
}

const regularStudents: student = {
  username: "roanmorgado",
  password: "1234",
  displayName : "Melo"
}
</script>

<template>
  <div>
    Hello Vue!!
    <p class = "pra">2026-09-19</p>
  </div>
</template>

<style>
*{
  font-family: "Courier New", Courier, monospace;
  color: purple;
}

.pra{
  text-align: center;
  padding: 20px 10px;
  background: aqua;
  corner-block-end-shape: round;

}
</style>