<script setup lang="ts">
import PlantComponent from '../components/PlantComponent.vue'

const onClick = () => {
  alert('Ouch!')
}
</script>

<template>
  <div class="flex h-screen w-screen flex-col items-center justify-center gap-4">
    <PlantComponent
      name="Lagundi"
      description="Lorem ipsum dolor sit amet consectetur, adipisicing elit. Quisquam, id?"
    />
    <button
      class="cursor-pointer rounded bg-orange-600 px-6 py-2 text-white hover:bg-orange-700"
      @click="onClick"
    >
      Click me
    </button>
    <PlantComponent
      name="Gumamela"
      description="Lorem ipsum dolor sit amet consectetur, adipisicing elit. Quisquam, id?"
    />
    <PlantComponent
      name="Cactus"
      description="Lorem ipsum dolor sit amet consectetur, adipisicing elit. Quisquam, id?"
    />
  </div>
</template>