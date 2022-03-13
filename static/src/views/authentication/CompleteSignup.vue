<template>
    <Base ref="base">
        <template #page_content>
            <div class="row justify-center q-pa-md">
                <q-card class="form-card__complete-signup">
                    <q-card-section>
                        <q-input
                            label="First Name"
                            v-model="formData.first_name"
                            :error="formErrors.first_name !== ''"
                            :error-message="formErrors.first_name"
                        />
                    </q-card-section>
                    <q-card-section>
                        <q-input
                            label="Last Name"
                            v-model="formData.last_name"
                            :error="formErrors.last_name !== ''"
                            :error-message="formErrors.last_name"
                        />
                    </q-card-section>

                    <q-card-section>
                        <q-input
                            disable
                            label="Email"
                            v-model="formData.email"
                            type="email"
                        />
                    </q-card-section>
                    <q-card-section>
                        <q-input
                            label="Username"
                            v-model="formData.username"
                            :error="formErrors.username !== ''"
                            :error-message="formErrors.username"
                        />
                    </q-card-section>
                    <q-card-actions>
                        <q-btn
                            class="full-width"
                            color="secondary"
                            label="Complete Signup"
                            text-color="dark"
                            @click="completeSignup"
                        />
                    </q-card-actions>
                </q-card>
            </div>
        </template>
    </Base>
</template>

<script setup>
import {
    inject,
    onBeforeMount,
    onMounted,
    reactive,
    ref,
    watch,
} from "@vue/runtime-core";
import Base from "../../components/layouts/Base.vue";
import { fetchUserWithCredentials } from "../../composables/axios";
import getAuthUser from "../../composables/getAuthUser";
import postAuthUser from "../../composables/postAuthUser";
import getUrls from "../../composables/getUrls";

// const { routes, callUrls } = getUrls();
const base = ref(null);
onMounted(() => {
    console.log(base.value);
});
// const routes = inject("routes");

const { callAuthUser } = getAuthUser();
const { updateAuthUser } = postAuthUser();

const authUser = ref({});

const formData = reactive({
    first_name: "",
    last_name: "",
    username: "",
    email: "",
});

const formErrors = reactive({
    first_name: "",
    last_name: "",
    username: "",
    email: "",
});

onBeforeMount(async () => {
    authUser.value = await callAuthUser();
    formData.first_name = authUser.value.first_name;
    formData.last_name = authUser.value.last_name;
    formData.username = authUser.value.username;
    formData.email = authUser.value.email;
});

const completeSignup = async () => {
    // const res = await fetchUserWithCredentials.post(
    //     `/complete-signup/`,
    //     formData
    // );
    const res = await updateAuthUser(formData);

    if (res.status == 200) {
        console.log("completed ready for redirect");
        console.log(base.value.routes.login_redirect);
        window.location.href = base.value.routes.login_redirect;
        // window.location.replace(base.value.routes.login_redirect);
    } else {
        if (res.status == 400) {
            console.log(res.data);
            let errors = res.data;
            formErrors.first_name = errors?.first_name?.length
                ? errors.first_name[0]
                : "";
            formErrors.last_name = errors?.last_name?.length
                ? errors.last_name[0]
                : "";
            // formErrors.email = errors.email[0];
            formErrors.username = errors?.username?.length
                ? errors.username[0]
                : "";
        }
    }
};
</script>

<style lang="sass">
.form-card__complete-signup
    // width: calc( 60% * $breakpoint-sm-min )
    width: 100%
    @media (min-width: $breakpoint-sm-min)
        width: 60%

    @media (min-width: $breakpoint-md-min)
        width: 500px
</style>