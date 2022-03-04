<script setup>
import { OnClickOutside } from "@vueuse/components";
import { reactive } from "vue";
import { MAP_STYLES } from "../../utils/defaultSettings";
import DeckGL from "./DeckGL.vue";
import GeoJsonLayer from "./GeoJsonLayer.vue";
import Mapbox from "./Mapbox.vue";
import Popup from "./Popup.vue";
const accessToken =
  "pk.eyJ1IjoibXRyYWxrYSIsImEiOiJja2VjNm5hdWEwNjQ4MnZ0cHlycXlndnN5In0.mfQAFUPzfGZeMht0EToJBA";

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

const GEOJSON_DATA_URL =
  process.env.NODE_ENV === "development"
    ? "https://raw.githack.com/mtralka/CDN/main/napa-archeology-parcels.geojson"
    : "https://rawcdn.githack.com/mtralka/CDN/cc52ce62e9825fd029a63de43971bc32dc80dbe4/napa-archeology-parcels.geojson";
</script>

<template>
  <div w="full" h="full" class="relative">
    <DeckGL>
      <Mapbox
        :access-token="accessToken"
        :map-style="MAP_STYLES.OUTDOORS"
      ></Mapbox>
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
