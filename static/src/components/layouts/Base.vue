<template>
    <q-layout view="hHh lpR lFf">
        <CustomHeader />
        <q-page-container>
            <q-page style="max-width: 1440px" class="q-mx-auto">
                <slot name="page_content" :routes="routes" />
            </q-page>
        </q-page-container>
        <CustomFooter />
    </q-layout>
</template>

<script>
import { computed, ref } from "@vue/reactivity";
import CustomHeader from "./Header.vue";
import CustomFooter from "./Footer.vue";
import getUrls from "../../composables/getUrls";
import { onBeforeMount, onBeforeUnmount, provide } from "@vue/runtime-core";
import { useQuasar } from "quasar";

export default {
    name: "Base",
    components: {
        CustomHeader,
        CustomFooter,
    },
    setup() {
        const name = ref("my name");
        const $q = useQuasar();
        // const domain = window.location.origin;

        provide("domain", window.location.origin);

        const { callUrls } = getUrls();
        const routes = ref({});
        // onMounted(async () => {

        onBeforeMount(async () => {
            routes.value = await callUrls();
        });

        // console.log(routes.value);

        if (routes.value) {
            provide(
                "routes",
                computed(() => routes.value)
            );
        }

        // console.log($sizes.xl)
        onBeforeUnmount(() => {
            $q.loading.show({
                spinner: "QSpinnerPie",
            });
        });

        // })

        return { name, routes };
    },
};
</script>

<style lang="sass">
.card_link
    display: block
    text-decoration: none

// #base {
//  font-family: Avenir, Helvetica, Arial, sans-serif;
//  -webkit-font-smoothing: antialiased;
//  -moz-osx-font-smoothing: grayscale;
//  text-align: center;
//  color: #2c3e50;
//  margin-top: 60px;
// } 
</style>
