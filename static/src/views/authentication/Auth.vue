<template>
    <Base ref="base">
        <template #page_content>
            <div class="row justify-center q-pa-lg">
                <q-card class="form-card__complete-signup q-pb-lg">
                    <q-card-section class="text-center">
                        <span class="text-primary text-h5">
                            {{ formTitle }}
                        </span>
                    </q-card-section>

                    <q-separator size="1.5px" />

                    <q-card-section class="row justify-center q-mt-lg">
                        <q-btn
                            label="Continue with Google"
                            icon="img:https://cdn.cdnlogo.com/logos/g/35/google-icon.svg"
                            class="my-4 font-bold"
                        />
                    </q-card-section>

                    <div class="row q-px-lg justify-around">
                        <div class="col">
                            <q-separator spaced />
                        </div>
                        <div class="col text-center">
                            <span class="text-bold">OR</span>
                        </div>
                        <div class="col">
                            <q-separator spaced />
                        </div>
                    </div>

                    <q-form
                        :action="`${
                            formTitle.toLowerCase() == 'sign up'
                                ? routes?.auth_routes?.account_signup
                                : routes?.auth_routes?.account_login
                        }${redirect_query}`"
                        method="post"
                    >
                        <q-card-section
                            v-if="formErrors?.non_field_errors"
                            class="text-negative"
                        >
                            <p v-for="error in formErrors.non_field_errors">
                                {{ error.message }}
                            </p>
                        </q-card-section>
                        <input
                            name="csrfmiddlewaretoken"
                            type="hidden"
                            :value="$q.cookies.get('csrftoken')"
                        />
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

                        <q-card-actions class="row justify-center">
                            <q-btn
                                color="secondary"
                                text-color="dark"
                                :label="formTitle"
                                @click="submitAuth"
                                type="submit"
                                no-caps
                                size="md"
                            />
                        </q-card-actions>
                    </q-form>
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
import { inject, onBeforeMount, reactive } from "@vue/runtime-core";

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

const form_errors = inject("form_errors");
console.log(form_errors.__all__);

const formErrors = reactive({
    non_field_errors: form_errors.__all__ ?? "",
});
</script>

<style lang="sass">
.form-card__complete-signup
    margin-top: 70px
    width: 100%
</style>