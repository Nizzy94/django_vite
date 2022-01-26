<template>
    <q-toolbar>
        <!-- <div flex> -->
        <q-btn
            dense
            flat
            round
            icon="menu"
            @click="toggleLeftDrawerLocal"
            v-if="isSmallScreen"
        />
        <!-- {{ isSmallScreen }} -->

        <q-toolbar-title shrink>
            <a :href="routes?.home" id="toolbar_title">
                <q-avatar>
                    <img
                        src="https://cdn.quasar.dev/logo-v2/svg/logo-mono-white.svg"
                    />
                </q-avatar>
                Title
            </a>
        </q-toolbar-title>
        <q-space />

        <q-btn icon="mdi-magnify" stretch flat @click="openSearch" />
        <!-- <q-space /> -->
        <q-separator dark vertical />
        <q-btn-dropdown
            stretch
            flat
            label="Blog"
            v-if="!isSmallScreen"
            :class="{ 'nav-link-active': currentRouteIsBlog }"
        >
            <!-- :class="{ 'nav-link-active': routes?.blog?.includes(currentRoute) }" -->
            <navbar-blog-category :routes="routes" />
        </q-btn-dropdown>
        <q-separator dark vertical v-if="!isSmallScreen" />
        <q-btn
            stretch
            flat
            label="About Us"
            v-if="!isSmallScreen"
            :class="{ 'nav-link-active': currentRoute == routes?.about }"
            tag="a"
            :href="routes?.about"
        />
        <q-separator dark vertical v-if="!isSmallScreen" />
        <q-btn
            stretch
            flat
            label="Contact"
            v-if="!isSmallScreen"
            tag="a"
            :class="{ 'nav-link-active': currentRoute == routes?.contact }"
            :href="routes?.contact"
        />
        <q-separator dark vertical v-if="!isSmallScreen" />
        <q-btn
            color="secondary"
            unelevated
            :label="$q.screen.gt.md ? 'Account' : ''"
            stretch
            icon="mdi-account"
            text-color="dark"
            @click="openAccountDia"
        />
        <!-- </div> -->
    </q-toolbar>

    <search-dialog ref="search_d" />
    <account-dialog ref="account_d" />
    <!-- {{ routes }} -->
</template>

<script>
import NavbarBlogCategory from "../NavbarBlogCategory.vue";
// import drawerFunctionality from '../../composables/drawerFunctionality'
import { useQuasar } from "quasar";
import { computed, ref } from "@vue/reactivity";
import SearchDialog from "../SearchDialog.vue";
import AccountDialog from "../AccountDialog.vue";
import { inject, watch } from "@vue/runtime-core";
export default {
    components: { NavbarBlogCategory, SearchDialog, AccountDialog },
    emits: ["toggleDrawer"],
    // props: {
    //     routes: Object,
    // },

    setup(props, { emit }) {
        // const { toggleLeftDrawer} = drawerFunctionality()

        // const routes = computed(() => inject("routes").value);
        const routes = inject("routes");
        const currentRoute = ref(window.location.href);

        // console.log(routes.value)

        const $q = useQuasar();

        const toggleLeftDrawerLocal = () => {
            emit("toggleDrawer");
        };
        const search_d = ref(null);
        const account_d = ref(null);

        const openSearch = () => {
            search_d.value.openSearch();
        };
        const openAccountDia = () => {
            account_d.value.openAccountDia();
        };

        const isSmallScreen = computed(() => $q.screen.lt.md);

        const currentRouteIsBlog = ref(false);
        console.log(routes?.value);
        watch(routes, () => {
            console.log(routes.value);
            if (Object.keys(routes.value).length) {
                console.log(Object.values(routes.value));

                if (
                    Object.values(routes.value.blog).includes(
                        currentRoute.value
                    )
                ) {
                    currentRouteIsBlog.value = true;
                }

                for (let i = 0; i < routes.value.blog.categories.length; i++) {
                    const cat = routes.value.blog.categories[i];

                    if (cat.url == currentRoute.value) {
                        currentRouteIsBlog.value = true;
                    }
                }
            }
        });

        return {
            routes,
            currentRoute,
            search_d,
            account_d,
            toggleLeftDrawerLocal,
            isSmallScreen,
            openSearch,
            currentRouteIsBlog,
            openAccountDia,
        };
    },
};
</script>

<style lang="sass">
#toolbar_title
    text-decoration: none
    color: white

.q-toolbar
    max-width: 1440px !important
    margin: auto
</style>
<style lang="sass" scoped>
.nav-link-active
    border-bottom: 2px solid $secondary !important
    color: $secondary !important
    font-weight: bold !important
</style>