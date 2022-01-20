<template>
    <Base>
        <template #page_content>
            <div
                class="row q-mx-auto q-px-md q-mt-lg"
                :class="{ 'q-col-gutter-lg': $q.screen.gt.xs }"
            >
                <div class="col-sm-6 col-xs-12 q-mb-lg">
                    <div class="text-h4 text-primary">
                        Have anything to tell us?
                    </div>
                    <div class="text-body1">Send us a message below.</div>
                    <div class="row q-mt-md"
                        :class="{ 'q-col-gutter-md': $q.screen.gt.sm }"
                    >
                        <div class="col-md-6 col-xs-12">
                            <q-input
                                v-model="contactFormData.name"
                                hint="Enter full name"
                                hide-hint
                                label="Name"
                            />
                        </div>
                        <div class="col-md-6 col-xs-12">
                            <q-input
                                v-model="contactFormData.email"
                                type="email"
                                hint="Enter email address"
                                hide-hint
                                label="Email"
                            />
                        </div>
                    </div>
                    <div class="">
                        <q-input
                            v-model="contactFormData.subject"
                            label="Subject"
                            hint="Give subject to your message"
                            hide-hint
                        />
                    </div>
                    <div class="">
                        <q-input
                            v-model="contactFormData.message"
                            counter
                            maxlength="500"
                            outlined
                            autogrow
                            label="Message"
                            hint="Give message in details"
                            hide-hint
                        />
                    </div>
                    <div class="flex justify-center">
                        <q-btn
                            label="Send"
                            color="secondary"
                            text-color="dark"
                        />
                    </div>
                </div>
                <div class="col-sm-6 col-xs-12 q-mb-lg">
                    <div class="text-h4 text-primary">
                        Subscribe to our newsletter
                    </div>
                    <!-- <div class="text-body1">Send us a message below.</div> -->
                    <div class="" style="margin-top: 57px">
                        <q-input
                            v-model="subscriptionFormData.name"
                            hint="Enter full name"
                            hide-hint
                            label="Name"
                        />
                    </div>
                    <div class="">
                        <q-input
                            v-model="subscriptionFormData.email"
                            type="email"
                            hint="Enter email address"
                            hide-hint
                            label="Email"
                        />
                    </div>
                    <div class="flex justify-center">
                        <q-btn
                            label="Subscribe"
                            color="secondary"
                            text-color="dark"
                        />
                    </div>
                </div>
            </div>
        </template>
    </Base>
</template>

<script setup>
import { reactive } from "@vue/reactivity";
import Base from "../components/layouts/Base.vue";

const contactFormData = reactive({
    name: "",
    email: "",
    subject: "",
    message: "",
});
const subscriptionFormData = reactive({
    name: "",
    email: "",
});
</script>

<style>
</style>