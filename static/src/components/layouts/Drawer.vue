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
                        <q-expansion-item
                            label="BLOG"
                            :header-class="{
                                'text-primary': currentRouteIsBlog,
                            }"
                        >
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
                                'nav-link-active':
                                    currentRoute == routes?.about,
                            }"
                            tag="a"
                            :href="routes?.about"
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
                                    currentRoute == routes?.contact,
                            }"
                            :href="routes?.contact"
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
import { inject, watch } from "@vue/runtime-core";
// import { useStore } from 'vuex'
// import { watch } from '@vue/runtime-core'

export default {
    components: { NavbarBlogCategory },
    props: {
        routes: Object,
    },
    setup(props) {
        // const store = useStore()

        const { toggleLeftDrawer, leftDrawerOpen } = drawerFunctionality();
        const toggleDrawer = () => toggleLeftDrawer();

        // const routes = computed(() => inject("routes").value);
        const routes = inject("routes");
        const currentRoute = ref(window.location.href);

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
            toggleDrawer,
            leftDrawerOpen,
            routes,
            currentRoute,
            currentRouteIsBlog,
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