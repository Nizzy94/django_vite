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
        <section  style="height: 80vh" class="column justify-center">
          <latest-section />
        </section>
      </template>
  </Layout>
</template>

<script setup>
import Layout from "../components/layouts/Base.vue"
import Hero from "../components/Home/Hero.vue"
import CategorySection from "../components/Home/CategorySection.vue"
import LatestSection from "../components/Home/LatestSection.vue"
</script>


<style>

</style>
  