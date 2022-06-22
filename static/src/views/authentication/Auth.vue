<template>
    <Base ref="base">
        <template #page_content>
            <div class="row justify-center q-pa-md">
                <q-card class="form-card__complete-signup">
                    <q-card-section class="text-center">
                        <span class="text-primary text-h5">
                            {{ formTitle }}
                        </span>
                    </q-card-section>

                    <q-separator />

                    <slot name="form_controls" />

                    <q-card-section class="q-px-lg">
                        <p v-if="formTitle.toLowerCase() == 'sign in'">
                            Not having an account?
                            <q-btn
                                label="Sign Up"
                                dense
                                flat
                                color="primary"
                                no-caps
                                type="a"
                                :href="`/signup/auth/${redirect_query}`"
                            />
                            here.
                        </p>
                        <p v-else-if="formTitle.toLowerCase() == 'sign up'">
                            Already having an account?
                            <q-btn
                                label="Sign In"
                                dense
                                flat
                                color="primary"
                                no-caps
                                type="a"
                                :href="`/login/auth/${redirect_query}`"
                            />
                            here
                        </p>
                    </q-card-section>
                    <q-card-actions class="q-px-lg row justify-center">
                        <q-btn
                            color="secondary"
                            text-color="dark"
                            :label="formTitle"
                            @click="submitAuth"
                            no-caps
                        />
                    </q-card-actions>
                </q-card>
            </div>
        </template>
    </Base>
</template>

<script async setup>
import { ref, toRefs } from "vue";
import Base from "../../components/layouts/Base.vue";
import getUrls from "../../composables/getUrls";
import generateAuthUrls from "../../composables/generateAuthUrls";
import { onBeforeMount } from "@vue/runtime-core";

const props = defineProps({
    formTitle: {
        type: String,
        required: true,
    },
});

const { formTitle } = toRefs(props);

const { callUrls, routes } = getUrls();
const { generateLink, redirect_query } = generateAuthUrls();

const query = ref(window.location.search);
const queries = ref(new URLSearchParams(query.value));
const redirect_url = queries.value.get("next");
// const redirect_q = ref("");

onBeforeMount(async () => {
    await callUrls();

    await generateLink(routes, redirect_url);
});

const emit = defineEmits(["signIn", "signUp"]);

const submitAuth = () => {
    formTitle.value.toLowerCase() == "sign in"
        ? emit("signIn")
        : emit("signUp");
};
</script>

<style lang="sass">
.form-card__complete-signup
    margin-top: 80px
    width: 100%
</style>