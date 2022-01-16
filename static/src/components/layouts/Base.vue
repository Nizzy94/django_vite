<template>
  <q-layout view="hHh lpR lFf">
    <CustomHeader />
    <q-page-container style="">
      <q-page>
      <slot name="page_content" />
      </q-page>
    </q-page-container>
    <CustomFooter />
  </q-layout>
</template>

<script>
import { computed, ref } from "@vue/reactivity";
import CustomHeader from "./Header.vue";
import CustomFooter from "./Footer.vue";

import getUrls from "../../composables/getUrls"
import { provide } from '@vue/runtime-core';

export default {
  name: "Base",
  components: {
    CustomHeader,
    CustomFooter
  },
  setup() {
    const name = ref("my name");

    const {routes, callUrls} = getUrls()

    // onMounted(async () => {

       callUrls()
       
       console.log(routes)

       if(routes.value) {

         provide('routes', computed(()=>routes.value))
       }
  
    // })




    return { name, routes };
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
