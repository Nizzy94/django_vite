<template>
  <q-toolbar>
        <q-btn dense flat round icon="menu" @click="toggleLeftDrawerLocal" v-if="isSmallScreen" />
        <!-- {{ isSmallScreen }} -->

        <q-toolbar-title shrink>
            <a :href="routes.home" id="toolbar_title">

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
        <q-btn stretch flat label="About Us" v-if="!isSmallScreen" tag="a" :href="routes.about" />
        <q-separator dark vertical v-if="!isSmallScreen" />
        <q-btn stretch flat label="Contact"  v-if="!isSmallScreen" tag="a" :href="routes.contact"/>
        <q-separator dark vertical v-if="!isSmallScreen" />
        <q-btn  color="white" stretch icon="mdi-account" flat @click="openAccountDia"  />

      </q-toolbar>

        <search-dialog ref="search_d" />
        <account-dialog ref="account_d" />
        <!-- {{ routes }} -->


</template>

<script>
import NavbarBlogCategory from '../NavbarBlogCategory.vue'
// import drawerFunctionality from '../../composables/drawerFunctionality' 
import {useQuasar} from 'quasar'
import { computed, ref } from '@vue/reactivity'
import SearchDialog from "../SearchDialog.vue"
import AccountDialog from "../AccountDialog.vue"
import { inject } from '@vue/runtime-core'
export default {
    components: { NavbarBlogCategory, SearchDialog, AccountDialog },
    emits: ['toggleDrawer'],
    
    setup (props,{emit}) { 
        // const { toggleLeftDrawer} = drawerFunctionality()

        const routes = computed(() => inject('routes').value)

        // console.log(routes.value)

        const $q = useQuasar()

        const toggleLeftDrawerLocal = () => {
            emit("toggleDrawer")
        }
        const search_d = ref(null)
        const account_d = ref(null)
        

        const openSearch = () => {search_d.value.openSearch()}
        const openAccountDia = () => {account_d.value.openAccountDia()}

        const isSmallScreen = computed(()=>$q.screen.lt.md)


        return{
          routes,
            search_d,
            account_d,
            toggleLeftDrawerLocal,
            isSmallScreen,
            openSearch,
            openAccountDia,
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