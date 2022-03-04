<script setup>
import { computed } from "vue";

const props = defineProps({
  targetPoint: {
    type: Object,
    required: true,
  },
});

const absX = computed(() => props.targetPoint.x + "px");
const absY = computed(() => props.targetPoint.y + "px");
</script>

<template>
  <div
    v-if="targetPoint.show && targetPoint.id"
    :class="targetPoint.show ? 'absolute' : 'hidden'"
    :style="{
      left: absX,
      top: absY,
    }"
    font="normal-nums"
    text="lg"
    p="2"
    rounded="xl"
    display="flex"
    flex="row"
    space="x-3"
    justify="center"
    items="center"
    bg="white"
  >
    <p><span font="bold">ASMT: </span>{{ targetPoint.id }}</p>
    <div
      @click="targetPoint.show = false"
      text="right gray-600 xs"
      font="bold"
      cursor="pointer"
      hover="underline text-gray-800"
    >
      X
    </div>
  </div>
</template>
