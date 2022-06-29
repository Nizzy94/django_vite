<template>
    <!-- <div class="text-body1">Send us a message below.</div> -->
    <div class="q-mb-md" style="">
        <q-input
            dense
            v-model="subscriptionFormData.first_name"
            hint="Enter firstname only"
            hide-hint
            label="Firstname"
            :error="subscriptionFormErrors.first_name != ''"
            :error-message="subscriptionFormErrors?.first_name"
        />
    </div>
    <div class="q-mb-md">
        <q-input
            v-model="subscriptionFormData.email"
            type="email"
            dense
            hint="Enter email address"
            hide-hint
            label="Email"
            :error="subscriptionFormErrors.email != ''"
            :error-message="subscriptionFormErrors?.email"
        />
    </div>
    <div class="flex justify-center">
        <q-btn
            label="Subscribe"
            @click="subscribe"
            color="secondary"
            text-color="dark"
            :loading="subscribing"
        />
    </div>
</template>

<script setup>
import { reactive, ref, toRefs } from "@vue/reactivity";
import { inject, watch } from "@vue/runtime-core";
import { fetchBlogAllowAny } from "../../composables/axios";
import { useQuasar } from "quasar";

const $q = useQuasar();

const props = defineProps({
    authUser: {
        type: Object,
        default: {},
    },
});

const { authUser } = toRefs(props);
console.log(authUser);

const routes = inject("routes");

const subscriptionFormData = reactive({
    first_name: "",
    email: "",
    url: window.location.href,
});
const subscriptionFormErrors = reactive({
    first_name: "",
    email: "",
});
watch(authUser, () => {
    if (Object.keys(authUser).length) {
        subscriptionFormData.first_name = authUser.value?.first_name;
        subscriptionFormData.email = authUser.value?.email;
    }
});

const subscribing = ref(false);

const subscribe = async () => {
    console.log(routes.value.blog.subscribe);
    subscribing.value = true;
    console.log("running");
    try {
        console.log("trying");
        const res = await fetchBlogAllowAny.post(
            routes.value.blog.subscribe,
            subscriptionFormData
        );

        if (res.status == 200) {
            console.log(res.data);
            $q.notify({
                type: "positive",
                message: res.data.message,
                position: "top-right",
            });
        }
    } catch (e) {
        console.log("error");

        if (e.response) {
            console.log(e.response.data);
            subscriptionFormErrors.first_name = e.response.data?.first_name
                ? e.response.data?.first_name[0]
                : "";
            subscriptionFormErrors.email = e.response.data?.email
                ? e.response.data?.email[0]
                : "";
        } else if (e.request) {
            console.log(e.request);
        }
    } finally {
        console.log("finally");

        subscribing.value = false;
    }
};
</script>

<style>
</style>