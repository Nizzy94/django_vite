<template>
    <ProfileGeneral>
        <template #form_content="{ routes }">
            <p class="q-mb-md">Are you sure you want to sign out?</p>
            <q-form
                @submit.prevent="submitLogout(routes)"
                method="post"
                :action="routes?.auth_routes?.account_logout"
                id="logout_form"
            >
                <CSRFToken />
                <!-- <div> -->
                <input
                    type="hidden"
                    v-if="redirect_field.value != 'None'"
                    :name="redirect_field.name"
                    :value="redirect_field.value"
                />

                <q-btn
                    label="Sign Out"
                    color="negative"
                    :loading="logingOut"
                    type="submit"
                />
                <!-- </div> -->
            </q-form>
        </template>
    </ProfileGeneral>
</template>

<script setup>
import CSRFToken from "../../components/CSRFToken.vue";
import ProfileGeneral from "../../components/auth/ProfileGeneral.vue";
import { inject, ref } from "@vue/runtime-core";
import axios from "axios";
import { Cookies } from "quasar";
import getQueries from "../../composables/getQueries";

const redirect_field = inject("redirect_field");
const logingOut = ref(false);

const { getRedirectUrl } = getQueries();

const redirect_url = getRedirectUrl();

const submitLogout = async (routes) => {
    logingOut.value = true;
    // const form = document.getElementById("logout_form");

    console.log(routes);

    axios
        .post(
            routes?.auth_routes?.rest_logout,
            {},
            {
                headers: {
                    "X-CSRFToken": Cookies.get("csrftoken"),
                },
                // withCredentials: true,
            }
        )
        .then((res) => {
            // console.log(redirect_field);
            const red_q = getRedirectUrl();
            // console.log(red_q);
            window.location.replace(red_q);
        })
        .catch((e) => {
            if (e.response) {
                console.log(e.response);
            } else if (e.request) {
                console.log(e.request);
            } else {
                console.log(e);
            }
        })
        .finally(() => {
            logingOut.value = false;
        });

    // form.submit();
};
</script>

<style>
</style>