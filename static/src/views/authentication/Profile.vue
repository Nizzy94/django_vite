<template>
    <ProfileGeneral>
        <template #form_content="{ routes }">
            <div class="form_content">
                <div class="row justify-between q-col-gutter-md">
                    <div class="col-12">
                        <q-input
                            name="first_name"
                            label="First Name"
                            v-model="formData.first_name"
                            :error="formErrors.first_name !== ''"
                            :error-message="formErrors.first_name"
                        />
                    </div>
                    <div class="col-12">
                        <q-input
                            name="last_name"
                            label="Last Name"
                            v-model="formData.last_name"
                            :error="formErrors.last_name !== ''"
                            :error-message="formErrors.last_name"
                        />
                    </div>
                </div>

                <div class="row justify-between q-col-gutter-md">
                    <div class="col-12">
                        <q-input
                            label="Email"
                            name="email"
                            disable
                            v-model="formData.email"
                            :error="formErrors.email !== ''"
                            :error-message="formErrors.email"
                            type="email"
                        />
                    </div>
                    <div class="col-12">
                        <q-input
                            name="username"
                            label="Username"
                            v-model="formData.username"
                            :error="formErrors.username !== ''"
                            :error-message="formErrors.username"
                        />
                    </div>
                </div>
                <div class="row justify-center">
                    <q-btn
                        label="Update Profile"
                        type="submit"
                        color="secondary"
                        :loading="updating"
                        text-color="dark"
                        @click="updateProfile(routes)"
                    />
                </div>
            </div>
        </template>
    </ProfileGeneral>
</template>

<script setup>
import { reactive, ref } from "@vue/reactivity";
import { inject, onBeforeMount } from "@vue/runtime-core";
import axios from "axios";
import { Cookies } from "quasar";
import ProfileGeneral from "../../components/auth/ProfileGeneral.vue";
import getUrls from "../../composables/getUrls";
import { useQuasar } from "quasar";

const { callUrls } = getUrls();
const old_form_data = inject("old_form_data");
const form_errors = inject("form_errors");
const updating = ref(false);
const $q = useQuasar();

const formData = reactive({
    first_name: old_form_data ? old_form_data.first_name : "",
    last_name: old_form_data ? old_form_data.last_name : "",
    username: old_form_data ? old_form_data.username : "",
    email: old_form_data ? old_form_data.email : "",
});
const formErrors = reactive({
    first_name: form_errors.first_name ? form_errors.first_name[0].message : "",
    last_name: form_errors.last_name ? form_errors.last_name[0].message : "",
    username: form_errors.username ? form_errors.username[0].message : "",
    email: form_errors.email ? form_errors.email[0].message : "",
});

const routes = ref({});
const user = ref({});

onBeforeMount(async () => {
    routes.value = await callUrls();
    let userResp = await axios.get(
        routes.value?.auth_routes?.rest_user_details
    );

    if (userResp.status == 200) {
        user.value = userResp.data;
        formData.first_name = user.value.first_name;
        formData.last_name = user.value.last_name;
        formData.username = user.value.username;
        formData.email = user.value.email;
    }
    // console.log(user.value);
});

const updateProfile = (routes) => {
    updating.value = true;
    const sending = $q.notify({
        type: "ongoing",
        message: "Updating profile ...",
        position: "top-right",
    });
    axios
        .post(routes.auth_routes.profile_api, formData, {
            headers: {
                "X-CSRFToken": Cookies.get("csrftoken"),
            },
            withCredentials: true,
        })
        .then((res) => {
            console.log(res);
            sending({
                type: "positive",
                message: "Profile updated successfully.",
                position: "top-right",
            });
        })
        .catch((e) => {
            if (e.response) {
                console.log(e.response);
                let errors = e.response.data;
                formErrors.first_name = errors.first_name
                    ? errors.first_name[0]
                    : "";
                formErrors.last_name = errors.last_name
                    ? errors.last_name[0]
                    : "";
                formErrors.username = errors.username ? errors.username[0] : "";
                formErrors.email = errors.email ? errors.email[0] : "";
                sending({
                    type: "negative",
                    message: "There was an error!",
                    position: "top-right",
                });
            } else if (e.request) {
                console.log(e.request);
            } else {
                console.log(e);
            }
        })
        .finally(() => {
            updating.value = false;
            // sending({
            //     type: "positive",
            //     message: "",
            //     timeout: 10,
            // });
        });
};
</script>

<style lang="sass">
.form_content
    width: 100%
    @media (min-width: $breakpoint-md-min)
        width: 70%
    @media (min-width: $breakpoint-lg-min)
        width: 50%
</style>