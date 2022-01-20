<template>
  <q-header reveal class="bg-primary text-white">
      <Navbar @toggleDrawer="triggerDrawer" />
      
    </q-header>

    <Drawer ref="drawer" />

</template>

<script>
// import drawerFunctionality from '../../composables/drawerFunctionality'
import Navbar from "./Navbar.vue"
import Drawer from "./Drawer.vue"
import { ref } from '@vue/reactivity'
export default {
    // mixins: [drawerFunctionality],
    components: {
        Navbar,
        Drawer
    },
    setup () {
        // const {leftDrawerOpen} = drawerFunctionality()
        const drawer = ref("")

        const triggerDrawer=()=> drawer.value.toggleDrawer()

        return{
            drawer,
            triggerDrawer
        }
    }

}
</script>

<style>

</style>