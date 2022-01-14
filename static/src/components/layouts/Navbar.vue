<template>
  <q-toolbar>
        <q-btn dense flat round icon="menu" @click="toggleLeftDrawerLocal" v-if="isSmallScreen" />
        <!-- {{ isSmallScreen }} -->

        <q-toolbar-title shrink>
            <a href="#" id="toolbar_title">

              <q-avatar>
                <img src="https://cdn.quasar.dev/logo-v2/svg/logo-mono-white.svg">
              </q-avatar>
              Title
            </a>
          </q-toolbar-title>
          <q-space />

        <q-btn icon="mdi-magnify" stretch flat @click="openSearch"  />
          <!-- <q-space /> -->
        <q-separator dark vertical />
        <q-btn-dropdown stretch flat label="Blog" v-if="!isSmallScreen">
          <navbar-blog-category />
        </q-btn-dropdown>
        <q-separator dark vertical v-if="!isSmallScreen" />
        <q-btn stretch flat label="About Us" v-if="!isSmallScreen" />
        <q-separator dark vertical v-if="!isSmallScreen" />
        <q-btn stretch flat label="Contact"  v-if="!isSmallScreen"/>
        <q-separator dark vertical v-if="!isSmallScreen" />
        <q-btn  color="white" stretch icon="mdi-account" flat />

      </q-toolbar>

        <search-dialog ref="search_d" >
          <!-- <template #input_field>
            <q-input dense v-model="search_term" autofocus @keyup.enter="search_d = false" />
          </template> -->
        </search-dialog>


</template>

<script>
import NavbarBlogCategory from '../NavbarBlogCategory.vue'
// import drawerFunctionality from '../../composables/drawerFunctionality' 
import {useQuasar} from 'quasar'
import { computed, ref } from '@vue/reactivity'
import SearchDialog from "../SearchDialog.vue"
export default {
    components: { NavbarBlogCategory, SearchDialog },
    emits: ['toggleDrawer'],
    
    setup (props,{emit}) { 
        // const { toggleLeftDrawer} = drawerFunctionality()

        const $q = useQuasar()

        const toggleLeftDrawerLocal = () => {
            // toggleLeftDrawer()
            emit("toggleDrawer")
        }

        // const search_term= ref("")


        const search_d = ref(null)
        console.log(search_d.value)

        const openSearch = () => {search_d.value.openSearch()}

        const isSmallScreen = computed(()=>$q.screen.lt.md)


        return{
            // leftDrawerOpen,
            search_d,
            toggleLeftDrawerLocal,
            isSmallScreen,
            openSearch,
            // search_term,
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