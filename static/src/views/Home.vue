<template>
  <Layout>
      <template #page_content>
          Home
          <div class="q-pa-md q-gutter-sm">
    <q-btn color="white" icon="menu" text-color="black" label="Standard" />
    <q-btn color="primary" icon="mdi-account-lock" label="Primary" />
    <q-btn color="secondary" label="Secondary" />
    <q-btn color="amber" glossy label="Amber" />
    <q-btn color="brown-5" label="Brown 5" />
    <q-btn color="deep-orange" glossy label="Deep Orange" />
    <q-btn color="purple" label="Purple" />
    <q-btn color="black" label="Black" />
  </div>
      </template>
  </Layout>
</template>

<script setup>
import Layout from "../components/layouts/Base.vue"
</script>

<style>

</style>
  