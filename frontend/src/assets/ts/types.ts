export type SightKeyword = 'Искусственное' | 'Природное'

export interface Sight {
    id: number
    title: string,
    description: string,
    images: string[] // массив url
    address: string
    latitude: number // вещественное число - широта
    longitude: number // вещественное число - долгота
    keywords: SightKeyword[]
}

export interface ApiResponce<DataType> {
    status: boolean
    data: DataType
}