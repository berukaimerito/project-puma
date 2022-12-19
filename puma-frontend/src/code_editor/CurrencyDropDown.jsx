import React from 'react'
import Select from 'react-select'
import { styles as customStyles } from '../constants/styles'
import { currencies } from '../constants/currencies'

const CurrencyDropDown = ({ handleCurrencyChange, currencyId }) => {
  return (
    <Select
      placeholder={`Select Currency`}
      options={currencies}
      styles={customStyles}
      defaultValue={currencyId ? currencies.filter(curr => curr.value === currencyId) : currencies[0]}
      onChange={(selectedOption) => handleCurrencyChange(selectedOption)}
    />
  )
}

export default CurrencyDropDown
