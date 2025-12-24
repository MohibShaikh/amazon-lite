<script setup lang="ts">
import { reactive } from "vue";
let initState = reactive({count: 0})
const decreaseCount = () => {
  if (initState.count > 0)
    initState.count--;
}
</script>
<template>
<!--  <h1>You did it!</h1>-->
  <Face />
<!--  <h2>{{initState.count}}</h2>-->
<!--  <Face />-->
<!--  <p>-->
<!--    Visit <a href="https://vuejs.org/" target="_blank" rel="noopener">vuejs.org</a> to read the-->
<!--    documentation-->
<!--  </p>-->
<!--  <button @click="initState.count++">Incremental</button>-->
<!--  <button @click="initState.count=0">Resetter</button>-->
<!--  <button @click="decreaseCount">Decremental</button>-->
</template>

<style scoped></style>
