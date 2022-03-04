<script setup>
import Map from "./components/Map/Map.vue";
</script>

<template>
  <div
    display="flex"
    flex="col"
    justify="center"
    align="items-center"
    w="screen"
    h="screen"
    space="y-5"
    bg="cyan-700"
  >
    <header
      space="y-1"
      p="4"
      w="90vw"
      border="rounded-md"
      shadow="sm cyan-900"
      overflow="hidden"
      class="bg-[#75cff0]"
    >
      <h1 font="bold tracking-wide" text="3xl">Napa's Archeology</h1>
      <p font="medium tracking-tighter">
        Public parcels with potential archeological sites
      </p>
    </header>
    <Map
      w="90vw"
      h="75vh"
      border="rounded-md"
      shadow="md cyan-900"
      overflow="hidden"
    ></Map>
    <footer
      display="flex"
      justify="center"
      align="items-center"
      font="bold tracking-tighest"
      text="cyan-50"
    >
      <p>
        Made with ❤️ by
        <a href="https://tralka.xyz" target="_blank">Matthew</a>
      </p>
    </footer>
  </div>
</template>

<style>
#app {
  /* font-family: Avenir, Helvetica, Arial, sans-serif; */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
</style>
