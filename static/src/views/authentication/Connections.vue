<template>
    <ProfileGeneral>
        <template #form_content="{ routes }">
            <div class="form_content">
                <div class="q-mb-xl">
                    <div class="text-h5">Account Connections</div>
                    <!-- {{ social_accounts.count }} -->

                    <div v-if="social_accounts.count >= 1">
                        <p>
                            You can sign in to your account using any of the
                            following third party accounts:
                        </p>

                        <div>
                            <form action="" method="POST">
                                <q-table
                                    card-container-class="q-pa-none"
                                    :rows="rows"
                                    :columns="columns"
                                    title=""
                                    row-key="account"
                                    selection="single"
                                    v-model:selected="selectedAccountModel"
                                    separator="none"
                                    bordered
                                    hide-header
                                    @update:selected="updateSelectedAccount"
                                    flat
                                >
                                    <template v-slot:body-selection="scope">
                                        <q-checkbox
                                            v-model="scope.selected"
                                            size="sm"
                                        />
                                        <input
                                            name="account"
                                            type="radio"
                                            :value="scope.row.account.id"
                                            :checked="scope.selected"
                                            hidden
                                        />
                                        <!-- {{ scope }} -->
                                        <CSRFToken />
                                    </template>
                                    <template v-slot:body-cell-icon="props">
                                        <q-td
                                            :props="props"
                                            style="width: 20px"
                                        >
                                            <div>
                                                <q-icon
                                                    :name="`img:${props.value}`"
                                                    size="20px"
                                                />
                                            </div>
                                            <!-- <div class="my-table-details">
                                        {{ props.row.details }}
                                    </div> -->
                                        </q-td>
                                    </template>
                                    <!-- <q-radio
                                v-for="account in social_accounts.results"
                                :key="account.id"
                                name="account"
                                v-model="selectedAccount"
                                :val="account.provider"
                                :label="`${
                                    social_icons.find(
                                        (icon) =>
                                            icon.provider.toLowerCase() ==
                                            account.provider.toLowerCase()
                                    ).icon
                                } ${account.provider[0].toUpperCase()}${account.provider.slice(
                                    1
                                )}`"
                            /> -->
                                    <template v-slot:bottom>
                                        <div class="row">
                                            <q-btn
                                                label="Remove"
                                                color="negative"
                                                class="q-mr-sm q-mb-sm"
                                                @click="openRemoveAccountDialog"
                                                no-caps
                                            />
                                        </div>
                                    </template>
                                </q-table>
                            </form>
                            <RemoveAccountDialog
                                :selected_account="selectedAccount"
                                :routes="routes"
                                :ref="`removeAccountDialogRef`"
                            />
                        </div>
                    </div>

                    <div v-else>
                        <p class="q-mb-md">
                            You currently have no social network accounts
                            connected to this account.
                        </p>
                    </div>
                </div>

                <div>
                    <div class="text-h6 q-mb-md">Add a 3rd Party Account</div>
                    <!-- {{ social_icons }} -->
                    <div
                        v-for="provider in social_providers"
                        :key="provider.provider_id"
                    >
                        <q-btn
                            :label="provider.provider_name"
                            :icon="
                                social_icons.length
                                    ? `img:${
                                          social_icons.find(
                                              (icon) =>
                                                  icon.provider.toLowerCase() ==
                                                  provider.provider_id.toLowerCase()
                                          ).icon
                                      }`
                                    : ''
                            "
                            style="width: 200px"
                            :class="{ 'full-width': $q.screen.lt.sm }"
                            type="a"
                            :href="provider.provider_url"
                        />
                    </div>
                </div>
            </div>
        </template>
    </ProfileGeneral>
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
import axios from "axios";
import getUrls from "../../composables/getUrls";
import ProfileGeneral from "../../components/auth/ProfileGeneral.vue";
import CSRFToken from "../../components/CSRFToken.vue";
import RemoveAccountDialog from "../../components/auth/RemoveAccountDialog.vue";

const { callUrls } = getUrls();
const routes = ref({});
const selectedAccountModel = ref([]);
const selectedAccount = ref({});
const social_icons = ref([]);
onBeforeMount(async () => {
    routes.value = await callUrls();
    await axios
        .get(routes.value?.auth_routes?.social_icon_api)
        .then((res) => {
            console.log(res.data);
            social_icons.value = res.data;
        })
        .catch((e) => {
            if (e.response) {
                console.log(e.response);
            } else if (e.request) {
                console.log(e.request);
            } else {
                console.log(e);
            }
        });

    // await axios
    //     .get(routes.value?.auth_routes?.social_providers_api)
    //     .then((res) => {
    //         console.log(res);
    //     })
    //     .catch((e) => {
    //         if (e.response) {
    //             console.log(e.response);
    //         } else if (e.request) {
    //             console.log(e.request);
    //         } else {
    //             console.log(e);
    //         }
    //     });
});

const social_providers = inject("providers");
const social_accounts = ref([]);

// const form_account = inject("form_account");
const rows = ref([]);
watch(routes, async () => {
    if (Object.keys(routes.value).length) {
        console.log(routes.value);
        axios
            .get(routes.value?.auth_routes?.social_account_list)
            .then((res) => {
                social_accounts.value = res.data;
                // console.log(res.data);

                if (social_accounts.value?.results?.length) {
                    let results = social_accounts.value.results;

                    results.forEach((account) => {
                        rows.value.push({
                            icon: social_icons.value.find(
                                (icon) =>
                                    icon.provider.toLowerCase() ==
                                    account.provider.toLowerCase()
                            ).icon,
                            account: account,
                        });

                        // axios
                        //     .get(`${routes.value?.auth_routes?.account.provider}_connect`)
                        //     .then((res) => {
                        //         console.log(res);
                        //     })
                        //     .catch((e) => {
                        //         if (e.response) {
                        //             console.log(e.response);
                        //         } else if (e.request) {
                        //             console.log(e.request);
                        //         } else {
                        //             console.log(e);
                        //         }
                        //     });
                    });
                }
            })
            .catch((e) => {
                if (e.response) {
                    console.log(e.response);
                } else if (e.request) {
                    console.log(e.request);
                } else {
                    console.log(e);
                }
            });
        // console.log(res);
    }
});

const removeAccountDialogRef = ref(null);
const openAccountDialog = ref(false);

const openRemoveAccountDialog = () => {
    console.log(Object.keys(selectedAccount.value).length);
    if (Object.keys(selectedAccount.value).length) {
        console.log(removeAccountDialogRef.value);
        removeAccountDialogRef.value.openConfirmDialog = true;
    } else {
        removeAccountDialogRef.value.openSelectNotifyDialog = true;
    }
};

const updateSelectedAccount = (selection) => {
    console.log(selection);
    if (selection.length) {
        selectedAccount.value = selection[0].account;
    }
};

const columns = [
    {
        name: "icon",
        required: true,
        label: "Icon",
        align: "center",
        field: "icon",
        // format: val => `${val}`,
        sortable: false,
    },
    {
        name: "account",
        required: true,
        label: "Account",
        align: "left",
        field: "account",
        format: (val) =>
            `${val.provider[0].toUpperCase()}${val.provider.slice(1)}`,
        // format: (val) => `${val.provider}`,
        sortable: false,
    },
];
</script>

<style>
</style>