export const MAP_STYLES = {
  SATELLITE: "mapbox://styles/mapbox/satellite-v9",
  DARK: "mapbox://styles/mapbox/dark-v10",
  LIGHT: "mapbox://styles/mapbox/light-v10",
  OUTDOORS: "mapbox://styles/mapbox/outdoors-v11",
  STREETS: "mapbox://styles/mapbox/streets-v11",
};


export const INITIAL_VIEW_STATE = {
  latitude: 38.49213599908769,
  longitude: -122.38919241182482,
  zoom: 9,
  pitch: 0,
  bearing: 0,
};

export const MAPBOX_SETTINGS = {
  container: "map",
  width: "100%",
  style: MAP_STYLES.DARK,
  interactive: false,
  center: [INITIAL_VIEW_STATE.longitude, INITIAL_VIEW_STATE.latitude],
  zoom: INITIAL_VIEW_STATE.zoom,
  bearing: INITIAL_VIEW_STATE.bearing,
  pitch: INITIAL_VIEW_STATE.pitch,
};

export const DECKGL_SETTINGS = {
  canvas: "deck-canvas",
  width: "100%",
  height: "100%",
  controller: true,
  initialViewState: INITIAL_VIEW_STATE,
};
