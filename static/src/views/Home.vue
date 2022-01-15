<template>
  <Layout>
      <template #page_content>
        <section class="">
          <div class=" window-height">
            <hero />
          </div>
        </section>
        <section class="q-my-xl">
         <category-section />
        </section>
        <section style="margin-top:150px; margin-bottom:150px"   class="column justify-center">
          <latest-section />
        </section>
        <section style="margin-top:150px; margin-bottom:150px"  class=" justify-center">
          <news-section />
        </section>
        <section style="padding-top:100px;"  >
          <Author />
        </section>
        <!-- <section style=" padding-bottom:100px"  >
          <Author />
        </section> -->
      </template>
  </Layout>
</template>

<script setup>
import Layout from "../components/layouts/Base.vue"
import Hero from "../components/Home/Hero.vue"
import CategorySection from "../components/Home/CategorySection.vue"
import LatestSection from "../components/Home/LatestSection.vue"
import NewsSection from "../components/Home/NewsSection.vue"
import Author from "../components/Home/Author.vue"
</script>


<style>

</style>
  