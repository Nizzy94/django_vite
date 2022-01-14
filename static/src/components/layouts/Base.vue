<template>
  <q-layout view="hHh lpR lFf">
    <CustomHeader />
    <q-page-container style="">
      <q-page>
      <slot name="page_content" />
      </q-page>
    </q-page-container>
  </q-layout>
</template>

<script>
import { ref } from "@vue/reactivity";
import CustomHeader from "./Header.vue";

export default {
  name: "Base",
  components: {
    CustomHeader,
  },
  setup() {
    const name = ref("my name");
    return { name };
  },
};
</script>

<style>
@charset "UTF-8";
/* #base {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
} */
</style>
