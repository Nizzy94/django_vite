<template>
<!-- {{ leftDrawerOpen }} -->
  <q-drawer
  v-model="leftDrawerOpen"
  side="left"
  overlay
  behavior="mobile"
  elevated
>
      <div class="flex justify-end">
                <q-btn
                    icon="close"
                    class=""
                    densed
                    flat
                    round
                    @click="toggleDrawer"
                />
            </div>

    </q-drawer>

</template>

<script>
// import { computed, ref } from '@vue/reactivity'
import drawerFunctionality from "../../composables/drawerFunctionality"
// import { useStore } from 'vuex'
// import { watch } from '@vue/runtime-core'

export default {
    setup () {
        // const store = useStore()
        
        const { toggleLeftDrawer, leftDrawerOpen} = drawerFunctionality() 
        const toggleDrawer = () =>  toggleLeftDrawer() 


        // const leftDrawerOpenLocal = ref(false)


        // const leftDrawerOpen = computed(() => store.state.leftDrawerOpen)
        // watch(leftDrawerOpen, () => {
        //     leftDrawerOpenLocal.value = leftDrawerOpen.value
        //     console.log(leftDrawerOpenLocal.value)
        // })
        // console.log(leftDrawerOpen.value)

        return {
            toggleDrawer,
            leftDrawerOpen

        }
    }
}
</script>

<style>

</style>