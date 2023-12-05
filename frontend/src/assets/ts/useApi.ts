import { ApiResponce, Sight } from '@types'
import { ofetch } from 'ofetch'

const serverURL = 'http://127.0.0.1:5000'

export const useApi = () => ({
    useSightApi: () => sightApi
})

const sightApi = {
    getAll: async () => {
        const responce = await ofetch<ApiResponce<Sight[] | string>>(`${serverURL}/sights`, {
            method: 'GET',
        })
        return responce
    },
    get: async (id: number) => {
        const responce = await ofetch<ApiResponce<Sight | string>>(`${serverURL}/sights`, {
            method: 'GET',
            params: {
                id: id
            },
        })
        return responce
    }
}
