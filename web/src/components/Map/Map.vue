<script setup>
import { OnClickOutside } from "@vueuse/components";
import { reactive, ref } from "vue";
import { MAP_STYLES } from "../../utils/defaultSettings";
import BaseLayerSelect from "../BaseLayerSelect.vue";
import Popup from "../Popup.vue";
import DeckGL from "./DeckGL.vue";
import GeoJsonLayer from "./GeoJsonLayer.vue";
import Mapbox from "./Mapbox.vue";
const accessToken =
  "pk.eyJ1IjoibXRyYWxrYSIsImEiOiJja2VjNm5hdWEwNjQ4MnZ0cHlycXlndnN5In0.mfQAFUPzfGZeMht0EToJBA";

const mapStyle = ref(MAP_STYLES.OUTDOORS);
const clickedPolygon = reactive({
  show: null,
  id: null,
  x: null,
  y: null,
});

const handleClick = ({ info }) => {
  const { object, x, y } = info;
  console.log(info);

  clickedPolygon.show = true;
  clickedPolygon.id = String(object.properties.id).padStart(12, "0");
  clickedPolygon.x = x;
  clickedPolygon.y = y;
};

const handleBaseLayerChange = (event) => {
  mapStyle.value = event;
};

const GEOJSON_DATA_URL =
  process.env.NODE_ENV === "development"
    ? "https://raw.githack.com/mtralka/CDN/main/napa-archeology-parcels.geojson"
    : "https://rawcdn.githack.com/mtralka/CDN/cc52ce62e9825fd029a63de43971bc32dc80dbe4/napa-archeology-parcels.geojson";
</script>

<template>
  <div w="full" h="full" class="relative">
    <BaseLayerSelect @changeLayer="handleBaseLayerChange"> </BaseLayerSelect>
    <DeckGL>
      <Mapbox :access-token="accessToken" :map-style="mapStyle"></Mapbox>
      <GeoJsonLayer
        :data="GEOJSON_DATA_URL"
        :pickable="true"
        :stroked="true"
        :filled="true"
        :getLineWidth="2"
        :getFillColor="[160, 160, 180, 90]"
        @click="handleClick"
      >
      </GeoJsonLayer>
    </DeckGL>
    <OnClickOutside @trigger="clickedPolygon.show = false">
      <Popup :targetPoint="clickedPolygon"></Popup>
    </OnClickOutside>

    <slot></slot>
  </div>
</template>
