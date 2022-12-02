import React, { useEffect, useState } from 'react'
import CodeEditorWindow from './CodeEditorWindow'
import axios from 'axios'
import { languages as languageOptions } from '../constants/languages'

import { ToastContainer, toast } from 'react-toastify'
import 'react-toastify/dist/ReactToastify.css'

import { defineTheme } from '../lib/defineTheme'
import useKeyPress from '../hooks/useKeyPress'
import OutputWindow from './OutputWindow'
import OutputDetails from './OutputDetails'
import ThemeDropdown from './ThemeDropdown'
import LanguagesDropdown from './LanguagesDropdown'
import { Button, Col, Row } from 'react-bootstrap'
import CurrencyDropDown from './CurrencyDropDown'
import { useParams } from 'react-router'
import scriptService from '../services/mock/script.service'

const javascriptDefault = `/**
* Default code.
*/


const basicFunction = () => {
 return 2+2;
};
console.log(basicFunction());
`

const Landing = () => {
  const [code, setCode] = useState(javascriptDefault)
  const [customInput, setCustomInput] = useState('')
  const [outputDetails, setOutputDetails] = useState(null)
  const [processing, setProcessing] = useState(null)
  const [theme, setTheme] = useState('cobalt')
  const [currency, setCurrency] = useState('BTC')
  const [language, setLanguage] = useState(languageOptions[0])

  const params = useParams()

  const enterPress = useKeyPress('Enter')
  const ctrlPress = useKeyPress('Control')

  const onSelectChange = (sl) => {
    console.log('selected Option...', sl)
    setLanguage(sl)
  }

  useEffect(() => {
    if (enterPress && ctrlPress) {
      console.log('enterPress', enterPress)
      console.log('ctrlPress', ctrlPress)
      handleCompile()
    }
  }, [ctrlPress, enterPress])
  const onChange = (action, data) => {
    switch (action) {
      case 'code': {
        setCode(data)
        break
      }
      default: {
        console.warn('case not handled!', action, data)
      }
    }
  }
  const handleCompile = () => {
    setProcessing(true)
    const formData = {
      language_id: language.id,
      // encode source code in base64
      source_code: btoa(code),
      stdin: btoa(customInput),
    }
    const options = {
      method: 'POST',
      url: 'https://judge0-ce.p.rapidapi.com/submissions',
      params: { base64_encoded: 'true', fields: '*' },
      headers: {
        'content-type': 'application/json',
        'Content-Type': 'application/json',
        'X-RapidAPI-Host': 'judge0-ce.p.rapidapi.com',
        'X-RapidAPI-Key': '8f5e0ceda6msh4b6c8b4f5ed2d33p15fe14jsne35df6a8539f',
      },
      data: formData,
    }

    axios
      .request(options)
      .then(function (response) {
        console.log('res.data', response.data)
        const token = response.data.token
        checkStatus(token)
      })
      .catch((err) => {
        let error = err.response ? err.response.data : err
        // get error status
        let status = err.response.status
        console.log('status', status)
        if (status === 429) {
          console.log('too many requests', status)

          showErrorToast(`Quota of 100 requests exceeded`, 10000)
        }
        setProcessing(false)
        console.log('catch block...', error)
      })
  }

  const checkStatus = async (token) => {
    const options = {
      method: 'GET',
      url: 'https://judge0-ce.p.rapidapi.com/submissions' + '/' + token,
      params: { base64_encoded: 'true', fields: '*' },
      headers: {
        'X-RapidAPI-Host': 'judge0-ce.p.rapidapi.com',
        'X-RapidAPI-Key': '8f5e0ceda6msh4b6c8b4f5ed2d33p15fe14jsne35df6a8539f',
      },
    }
    try {
      let response = await axios.request(options)
      let statusId = response.data.status?.id

      // Processed - we have a result
      if (statusId === 1 || statusId === 2) {
        // still processing
        setTimeout(() => {
          checkStatus(token)
        }, 2000)
        return
      } else {
        setProcessing(false)
        setOutputDetails(response.data)
        showSuccessToast(`Compiled Successfully!`)
        console.log('response.data', response.data)
        return
      }
    } catch (err) {
      console.log('err', err)
      setProcessing(false)
      showErrorToast()
    }
  }

  function handleThemeChange(th) {
    const theme = th
    console.log('theme...', theme)

    if (['light', 'vs-dark'].includes(theme.value)) {
      setTheme(theme)
    } else {
      defineTheme(theme.value).then((_) => setTheme(theme))
    }
  }

  function handleCurrencyChange(crr) {
    setCurrency(crr)
  }

  useEffect(() => {
    defineTheme('oceanic-next').then((_) =>
      setTheme({ value: 'oceanic-next', label: 'Oceanic Next' })
    )
  }, [])

  useEffect(() => {
    if (params.id) {
      console.log('test11111')
      const script = scriptService.getScriptById(params.id)
      console.log(script)
      setCode(script[0].code)
    }
    console.log(code)
  }, [code])

  const showSuccessToast = (msg) => {
    toast.success(msg || `Compiled Successfully!`, {
      position: 'top-right',
      autoClose: 1000,
      hideProgressBar: false,
      closeOnClick: true,
      pauseOnHover: true,
      draggable: true,
      progress: undefined,
    })
  }
  const showErrorToast = (msg, timer) => {
    toast.error(msg || `Something went wrong! Please try again.`, {
      position: 'top-right',
      autoClose: timer ? timer : 1000,
      hideProgressBar: false,
      closeOnClick: true,
      pauseOnHover: true,
      draggable: true,
      progress: undefined,
    })
  }

  return (
    <>
      <ToastContainer
        position="top-right"
        autoClose={2000}
        hideProgressBar={false}
        newestOnTop={false}
        closeOnClick
        rtl={false}
        pauseOnFocusLoss
        draggable
        pauseOnHover
      />

      <Row className="justify-content-md-start">
        <Col sm={2} className="px-4 py-2">
          <LanguagesDropdown onSelectChange={onSelectChange} />
        </Col>
        <Col sm={2} className="px-4 py-2">
          <ThemeDropdown handleThemeChange={handleThemeChange} theme={theme} />
        </Col>
        <Col sm={2} className="px-4 py-2">
          <CurrencyDropDown handleCurrencyChange={handleCurrencyChange} theme={theme} />
        </Col>
      </Row>
      <Row>
        <Col sm={8}>
          <CodeEditorWindow
            code={code}
            onChange={onChange}
            language={language?.value}
            theme={theme.value}
          />
        </Col>

        <Col sm={4}>
          <OutputWindow outputDetails={outputDetails} />
          <div className="flex flex-col items-end">
            <button style={{ color: 'green' }} onClick={handleCompile} disabled={!code}>
              {processing ? 'Processing...' : 'Compile and Execute'}
            </button>
            <button style={{ marginLeft: '10px', color: 'red' }}>{'Stop'}</button>
          </div>
          {outputDetails && <OutputDetails outputDetails={outputDetails} />}
          <div style={{ marginTop: '10px' }}>
            <Button size="lg" variant="success">
              {params.id ? 'Save Changes' : 'Save Script'}
            </Button>
          </div>
        </Col>
      </Row>
    </>
  )
}
export default Landing
