<script setup lang = "ts">
defineProps<{
    name: string
    description: string
}>()
</script>

<template>
    <div class = 'w-full'>
        <p class = "text-2xl text-orange-800"> Plant Name: {{ name }}</p>
        <p class = "text-xl text-orange-500"> Description: {{ description }}</p>

    </div>
</template>