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
      </template>
  </Layout>
</template>

<script setup>
import Layout from "../components/layouts/Base.vue"
import Hero from "../components/Home/Hero.vue"
import CategorySection from "../components/Home/CategorySection.vue"
</script>


<style>

</style>
  