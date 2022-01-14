<template>
  <q-dialog v-model="search_d" >
      <q-card style="min-width: 350px">
        <q-card-section>
          <div class="text-h6">Search</div>
        </q-card-section>

        <q-card-section class="q-pt-none">
          <q-input dense v-model="search_term" autofocus @keyup.enter="search_d = false" />
          <!-- <slot name=input_field /> -->
        </q-card-section>

        <q-card-actions align="right" class="text-primary">
          <q-btn flat label="Cancel" v-close-popup />
          <q-btn flat label="Search" v-close-popup />
        </q-card-actions>
      </q-card>
    </q-dialog>
</template>

<script setup>
import {defineProps, toRefs, ref, watch} from "vue"

// const props = defineProps({
//   search_d: Boolean,
// })
// const {search_d} = toRefs(props) 

// watch(search_d, () => {
//   console.log(search_d)
// })

const search_term= ref("")
const search_d = ref(false)



const openSearch = () => {search_d.value =true}

defineExpose({
  openSearch,
})


</script>

<style>

</style>