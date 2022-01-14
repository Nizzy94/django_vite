<template>
  <q-list>
    <q-item-label header>Folders</q-item-label>
    <q-item v-for="n in 3" :key="`x.${n}`" clickable v-close-popup tabindex="0">
        <q-item-section avatar>
            <q-avatar icon="mdi-folder" color="secondary" text-color="white" />
        </q-item-section>
        <q-item-section>
            <q-item-label>Category {{n}}</q-item-label>
            <q-item-label caption>February 22, 2016</q-item-label>
        </q-item-section>
        <q-item-section side>
            <q-icon name="info" />
        </q-item-section>
    </q-item>
</q-list>
</template>

<script>
export default {

}
</script>

<style>

</style>