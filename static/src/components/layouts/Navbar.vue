<template>
  <q-toolbar>
        <q-btn dense flat round icon="menu" @click="toggleLeftDrawerLocal" />

        <q-toolbar-title shrink>
          <a href="#" id="toolbar_title">

          <q-avatar>
            <img src="https://cdn.quasar.dev/logo-v2/svg/logo-mono-white.svg">
          </q-avatar>
          Title
          </a>
        </q-toolbar-title>
        <q-space />
        <q-btn dense unelevated color="white" text-color="dark" label="Login"  @click="toggleLeftDrawerLocal" />

      </q-toolbar>

</template>

<script>
// import drawerFunctionality from '../../composables/drawerFunctionality' 
export default {
    emits: ['toggleDrawer'],
    
    setup (props,{emit}) { 
        // const { toggleLeftDrawer} = drawerFunctionality()

        const toggleLeftDrawerLocal = () => {
            // toggleLeftDrawer()
            emit("toggleDrawer")
        }

        return{
            // leftDrawerOpen,
            toggleLeftDrawerLocal
        }
    } 
}

</script>

<style>

#toolbar_title{
  text-decoration: none;
  color: white;
}

</style>