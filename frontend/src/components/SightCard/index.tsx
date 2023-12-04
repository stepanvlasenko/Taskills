import { useTextFormat } from '../../hooks/useTextFormat'
import './styles.css'

interface SightCardProps {
    id: number
    title: string
    description: string
    image: string
}

export default function SightCard({id, title, description, image, ...props}: SightCardProps) {
    const textFormat = useTextFormat()

    return (
        <div className='sight-card'>
            <img className='sight-card__image' src={image} alt={title} />
            <div className='sight-card__inforamation'>
                <p className='sight-card__title text--ibm-400'>{title}</p>
                <div className='sight-card__container'>
                    <p className='sight-card__description text--roboto-400'>{description}</p>
                    {/* Change to React-Router's link */}
                    <a className='sight-card__link'>
                        <p className='sight-card__link-text text--roboto-400'>Подробнее</p>
                        <div className='sight-card__link-vertical-line'></div>
                        <img className='sight-card__link-image' src="/images/arrow-right.svg" />
                    </a>
                </div>
            </div>
        </div>
    )
}