<script setup>
import { GeoJsonLayer } from "@deck.gl/layers";
import { inject, useAttrs, watch } from "vue";

const attrs = useAttrs();
const updateLayer = inject("updateLayer");
const afterInitialRender = inject("afterInitialRender");
const emit = defineEmits(["click", "hover"]);

watch(
  () => [afterInitialRender, attrs],
  () => {
    createLayer();
  },
  { deep: true }
);

function createLayer() {
  updateLayer(
    new GeoJsonLayer({
      id: "geojson-layer",
      ...attrs,
      onClick: (info, event) => emit("click", { info, event }),
      onHover: (info, event) => emit("hover", { info, event }),
    })
  );
}
</script>
<template></template>
