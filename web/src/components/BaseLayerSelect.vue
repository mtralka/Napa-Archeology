<script setup>
import { OnClickOutside } from "@vueuse/components";
import { ref } from "vue";
import MapIcon from "~icons/bx/map-alt";
import { MAP_STYLES } from "../utils/defaultSettings";

const emit = defineEmits(["changeLayer"]);

const showLayerSelect = ref(false);

function handleLayerClick(event) {
  emit("changeLayer", event.target.value);
  showLayerSelect.value = false;
}
</script>

<template>
  <OnClickOutside @trigger="showLayerSelect = false">
    <div
      pos="absolute bottom-2 right-2"
      z="50"
      display="flex"
      flex="col-reverse"
      justify="center"
      items="end"
    >
      <div
        cursor="pointer"
        w="11"
        h="11"
        border="rounded-md"
        :class="[showLayerSelect ? 'bg-gray-500' : 'bg-gray-50']"
        shadow="light-500"
        display="flex"
        justify="center"
        items="center"
        p="1"
        m="t-3"
        @click="showLayerSelect = !showLayerSelect"
      >
        <MapIcon text="4xl black" />
      </div>
      <ul v-if="showLayerSelect" space="y-2.5">
        <li
          v-for="style in Object.entries(MAP_STYLES)"
          :key="style"
          cursor="pointer"
          p="1 x-1.5"
          bg="cyan-700"
          border="rounded-md"
          shadow="sm cyan-900"
          text="cyan-50 lowercase"
        >
          <input
            type="radio"
            :value="style[1]"
            name="radio"
            :id="style[0]"
            cursor="pointer"
            @change="handleLayerClick"
          />
          <label :for="style[0]" cursor="pointer">
            {{ style[0] }}
          </label>
        </li>
      </ul>
    </div>
  </OnClickOutside>
</template>

<style scoped>
input {
  visibility: hidden;
  display: none;
}
input:checked + label {
  @apply font-black;
}
</style>
