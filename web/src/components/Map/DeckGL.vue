<script setup>
import { Deck } from "@deck.gl/core";
import { onMounted, provide, reactive, ref, useAttrs } from "vue";
import { DECKGL_SETTINGS } from "../../utils/defaultSettings";

const attrs = useAttrs();
let deck = null;
const afterInitialRender = ref(false);

const viewState = reactive({
  latitude: 38.49213599908769,
  longitude: -122.38919241182482,
  zoom: 9,
  pitch: 0,
  bearing: 0,
});

const deckgl_layers = [];

onMounted(() => {
  deck = new Deck({
    onViewStateChange: ({ viewState }) => handleViewChange(viewState),
    layers: deckgl_layers,
    ...DECKGL_SETTINGS,
    ...attrs,
  });
  afterInitialRender.value = true;
});
function handleViewChange(newState) {
  viewState.longitude = newState.longitude;
  viewState.latitude = newState.latitude;
  viewState.zoom = newState.zoom;
  viewState.pitch = newState.pitch;
  viewState.bearing = newState.bearing;
}
function updateLayer(newLayer) {
  if (!deck) {
    console.log("NO DECK");
    return;
  }
  deckgl_layers.push(newLayer);
  //deck.setProps({ layers: [...deck.layers, newLayer] });
}

provide("viewState", viewState);
provide("updateLayer", updateLayer);
provide("afterInitialRender", afterInitialRender);
</script>

<template>
  <div class="relative h-full w-full">
    <div class="h-full w-full absolute top-0 left-0">
      <slot></slot>
      <canvas
        id="deck-canvas"
        class="h-full w-full absolute top-0 left-0"
      ></canvas>
    </div>
  </div>
</template>
