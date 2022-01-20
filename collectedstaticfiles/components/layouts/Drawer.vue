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
        <div>
            <q-list separator>
                <q-item clickable v-ripple>
                    <q-item-section>
                        <q-expansion-item label="BLOG">
                            <navbar-blog-category />
                        </q-expansion-item>
                    </q-item-section>
                </q-item>

                <q-item clickable v-ripple>
                    <q-item-section>
                        <q-btn
                            align="left"
                            flat
                            label="About Us"
                            :class="{
                                'nav-link-active': currentRoute == routes.about,
                            }"
                            tag="a"
                            :href="routes.about"
                        />
                    </q-item-section>
                </q-item>

                <q-item clickable v-ripple>
                    <q-item-section>
                        <q-btn
                            align="left"
                            flat
                            label="Contact"
                            tag="a"
                            :class="{
                                'nav-link-active':
                                    currentRoute == routes.contact,
                            }"
                            :href="routes.contact"
                        />
                    </q-item-section>
                </q-item>
            </q-list>
        </div>
    </q-drawer>
</template>

<script>
import { computed, ref } from "@vue/reactivity";
// import { computed, ref } from '@vue/reactivity'
import drawerFunctionality from "../../composables/drawerFunctionality";
import NavbarBlogCategory from "../NavbarBlogCategory.vue";
import { inject } from "@vue/runtime-core";
// import { useStore } from 'vuex'
// import { watch } from '@vue/runtime-core'

export default {
    components: { NavbarBlogCategory },
    setup() {
        // const store = useStore()

        const { toggleLeftDrawer, leftDrawerOpen } = drawerFunctionality();
        const toggleDrawer = () => toggleLeftDrawer();

        const routes = computed(() => inject("routes").value);
        const currentRoute = ref(window.location.href);

        return {
            toggleDrawer,
            leftDrawerOpen,
            routes,
            currentRoute,
        };
    },
};
</script>

<style lang="sass" scoped>
.nav-link-active
    border: none !important
    color: $primary !important
    // font-weight: bold !important
</style>