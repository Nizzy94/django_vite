<template>
    <ProfileGeneral>
        <template #form_content="{ routes }">
            <div>
                <form
                    :action="routes?.auth_routes?.account_email"
                    method="post"
                >
                    <q-table
                        card-container-class="q-pa-none"
                        :rows="rows"
                        :columns="columns"
                        title="E-mail Addresses"
                        row-key="email"
                        selection="single"
                        v-model:selected="selected"
                        separator="none"
                        bordered
                        @update:selected="updateSelectedEmail"
                        flat
                    >
                        <template v-slot:top>
                            <div class="column">
                                <div class="">
                                    <span class="text-h5">
                                        E-mail Addresses
                                    </span>
                                </div>
                                <div
                                    class=""
                                    v-if="messages.length"
                                    v-for="(message, i) in messages"
                                    :key="i"
                                >
                                    <span
                                        :class="{
                                            'text-negative':
                                                message.tag == 'error',
                                            'text-positive':
                                                message.tag == 'success',
                                            'text-info': message.tag == 'info',
                                            'text-warning':
                                                message.tag == 'warning',
                                        }"
                                    >
                                        {{ message.message }}
                                    </span>
                                </div>
                            </div>
                        </template>
                        <template v-slot:header="props">
                            <CSRFToken />
                        </template>
                        <template v-slot:body-selection="scope">
                            <q-checkbox v-model="scope.selected" size="sm" />
                            <input
                                name="email"
                                type="radio"
                                :value="scope.row.email"
                                :checked="scope.selected"
                                hidden
                            />
                            <!-- {{ scope.rowIndex }} -->
                            <!-- <RemoveEmailDialog
                                :ref="`removeEmailDialogRef`"
                                :selected_email="scope.row.email"
                                :openDialog="openEmailDialog"
                                :routes="routes"
                            /> -->
                        </template>
                        <template v-slot:bottom>
                            <div class="row">
                                <q-btn
                                    label="Make primary"
                                    color="secondary"
                                    text-color="dark"
                                    class="q-mr-sm q-mb-sm"
                                    type="submit"
                                    name="action_primary"
                                    no-caps
                                    :disable="selected[0].primary_status"
                                />
                                <q-btn
                                    label="Re-send verification"
                                    color="secondary"
                                    text-color="dark"
                                    class="q-mr-sm q-mb-sm"
                                    type="submit"
                                    name="action_send"
                                    no-caps
                                    :disable="selected[0].verification_status"
                                />
                                <q-btn
                                    label="Remove"
                                    color="negative"
                                    class="q-mr-sm q-mb-sm"
                                    @click="openEmailDialog"
                                    no-caps
                                    :disable="
                                        selected[0].primary_status ||
                                        emails.length == 1
                                    "
                                />
                            </div>
                        </template>
                    </q-table>
                </form>
            </div>
            <h5 class="text-h5">Add E-mail Address</h5>
            <form
                class="form_content"
                method="POST"
                :action="routes?.auth_routes?.account_email"
            >
                <CSRFToken />
                <div class="q-mb-md">
                    <q-input
                        name="email"
                        label="E-mail"
                        v-model="formData.email"
                        :error="formErrors.email !== ''"
                        :error-message="formErrors.email"
                    />
                </div>

                <div class="">
                    <q-btn
                        label="Add Email"
                        type="submit"
                        name="action_add"
                        color="secondary"
                        text-color="dark"
                    />
                </div>
            </form>
            <RemoveEmailDialog
                :ref="`removeEmailDialogRef`"
                :selected_email="selected_email"
                :openDialog="openEmailDialog"
                :routes="routes"
            />
        </template>
    </ProfileGeneral>
</template>

<script setup>
import { reactive, ref } from "@vue/reactivity";
import { inject, watch } from "@vue/runtime-core";
import ProfileGeneral from "../../components/auth/ProfileGeneral.vue";
import RemoveEmailDialog from "../../components/auth/RemoveEmailDialog.vue";
import CSRFToken from "../../components/CSRFToken.vue";

const emails = inject("emails");
const old_form_data = inject("old_form_data");
const form_errors = inject("form_errors");
const messages = inject("messages");

const formData = reactive({
    email: old_form_data.email,
});
const formErrors = reactive({
    email: form_errors.email ? form_errors.email[0].message : "",
});

const removeEmailDialogRef = ref(null);

const selected = ref([]);

const openEmailDialog = () => {
    // console.log(removeEmailDialogRef.value);
    removeEmailDialogRef.value.openConfirmDialog = true;
};
const selected_email = ref("");

const updateSelectedEmail = (selection) => {
    // console.log(selection[0].email);
    selected_email.value = selection[0].email;
};

const rows = ref([]);

if (emails.length) {
    rows.value = [];
    emails.forEach((email) => {
        rows.value.push({
            email: email.email,
            primary_status: email.primary,
            verification_status: email.verified,
        });
    });

    rows.value.forEach((row) => {
        // console.log(row);
        if (row.primary_status || row.length == 1) {
            selected.value.push(row);
        }
    });

    if (rows.value.length) {
        rows.value.sort((a, b) =>
            a.primary_status > b.primary_status ? -1 : 1
        );
    }
}

const columns = [
    {
        name: "email",
        required: true,
        label: "E-mail",
        align: "left",
        field: "email",
        // format: val => `${val}`,
        sortable: false,
    },
    {
        name: "primary_status",
        align: "left",
        label: "Pimary Status",
        field: "primary_status",
        format: (val) => (val ? "Primary" : ""),
        sortable: false,
    },
    {
        name: "verification_status",
        align: "left",
        label: "Verification Status",
        field: "verification_status",
        format: (val) => (val ? "Verified" : "Not Verified"),
        sortable: false,
    },
];
</script>

<style lang="sass">
// .form_content
//     width: 100%
//     @media (min-width: $breakpoint-md-min)
//         width: 70%
//     @media (min-width: $breakpoint-lg-min)
//         width: 50%
</style>