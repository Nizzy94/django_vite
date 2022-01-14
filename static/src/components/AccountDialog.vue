<template>
  <q-dialog v-model="account_d" transition-show="slide-down" transition-hide="slide-up" transition-duration="600">
      <q-card style="min-width: 350px">
        <q-card-section>
          <div class="text-h6">What would you like to do?</div>
        </q-card-section>

        <q-card-section class="q-pt-none">
            <div class="row justify-around">
                <q-btn color="primary" outline  label="Sign In" />
                <q-btn color="primary" label="Sign Up" />
            </div>
        </q-card-section>

        <!-- <q-card-actions align="right" class="text-primary">
          <q-btn flat label="Cancel" v-close-popup />
          <q-btn flat label="Search" v-close-popup />
        </q-card-actions> -->
      </q-card>
    </q-dialog>
</template>

<script setup>
import {ref} from "vue"

const account_d = ref(false)



const openAccountDia = () => account_d.value =true

defineExpose({
  openAccountDia,
})


</script>

<style>

</style>