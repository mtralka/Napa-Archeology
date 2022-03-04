<script setup>
import mapboxgl from "mapbox-gl";
import { inject, onMounted, useAttrs, watch } from "vue";
import { MAPBOX_SETTINGS, MAP_STYLES } from "../../utils/defaultSettings";

const props = defineProps({
  accessToken: {
    type: String,
    required: true,
  },
  mapStyle: {
    type: String,
    required: false,
    default: null,
  },
});

let map = null;
const attrs = useAttrs();
const viewState = inject("viewState");

const geolocate = new mapboxgl.GeolocateControl({
  positionOptions: {
    enableHighAccuracy: true,
  },
  trackUserLocation: true,
  showUserHeading: true,
});

onMounted(() => {
  mapboxgl.accessToken = props.accessToken;
  map = new mapboxgl.Map({
    ...MAPBOX_SETTINGS,
    ...attrs,
    center: [viewState.longitude, viewState.latitude],
    zoom: viewState.zoom,
    bearing: viewState.bearing,
    pitch: viewState.pitch,
    style: props.mapStyle || MAP_STYLES.OUTDOORS,
  });

  geolocate._updateCamera = () => {};
  map.addControl(geolocate);
});
watch(
  () => viewState,
  (state, prevState) => {
    handleMapChange(state);
  },
  { deep: true }
);

watch(
  () => props.mapStyle,
  (newStyle, oldStyle) => {
    map.setStyle(newStyle);
  },
  { deep: false }
);

function handleMapChange(viewState) {
  map.jumpTo({
    center: [viewState.longitude, viewState.latitude],
    zoom: viewState.zoom,
    bearing: viewState.bearing,
    pitch: viewState.pitch,
  });
}
</script>

<template>
  <div
    id="map"
    ref="map"
    class="w-full h-full absolute top-0 left-0 overflow-hidden"
  ></div>
</template>
