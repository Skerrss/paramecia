package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strings"
	"sync"
)

const rethrowPanic = "_____rethrow"

var colorReset = "\033[0m"
var colorGreen = "\033[32m"
var colorRed = "\033[31m"

type (
	E         interface{}
	exception struct {
		finally func()
		Error   E
	}
)

func Throw() {
	panic(rethrowPanic)
}

func This(f func()) (e exception) {
	e = exception{nil, nil}
	defer func() {
		e.Error = recover()
	}()
	f()
	return
}

func (e exception) Catch(f func(err E)) {
	if e.Error != nil {
		defer func() {
			if e.finally != nil {
				e.finally()
			}

			if err := recover(); err != nil {
				if err == rethrowPanic {
					err = e.Error
				}
				panic(err)
			}
		}()
		f(e.Error)
	} else if e.finally != nil {
		e.finally()
	}
}

func writeResultMagento(outputFile *os.File, result string) {
	_, err := outputFile.WriteString(result + "\n")
	if err != nil {
		log.Println("Error writing FTP result to output file:", err)
	}
}

func writeResultDrupal(outputFile *os.File, result string) {
	_, err := outputFile.WriteString(result + "\n")
	if err != nil {
		log.Println("Error writing FTP result to output file:", err)
	}
}

func writeResultKonoha(outputFile *os.File, result string) {
	_, err := outputFile.WriteString(result + "\n")
	if err != nil {
		log.Println("Error writing FTP result to output file:", err)
	}
}

func writeResultPhpmyadmin(outputFile *os.File, result string) {
	_, err := outputFile.WriteString(result + "\n")
	if err != nil {
		log.Println("Error writing FTP result to output file:", err)
	}
}

func writeResultMoodle(outputFile *os.File, result string) {
	_, err := outputFile.WriteString(result + "\n")
	if err != nil {
		log.Println("Error writing FTP result to output file:", err)
	}
}

func writeResultFTP(outputFile *os.File, result string) {
	_, err := outputFile.WriteString(result + "\n")
	if err != nil {
		log.Println("Error writing FTP result to output file:", err)
	}
}

func writeResultOwncloud(outputFile *os.File, result string) {
	_, err := outputFile.WriteString(result + "\n")
	if err != nil {
		log.Println("Error writing FTP result to output file:", err)
	}
}

func writeResultPresta(outputFile *os.File, result string) {
	_, err := outputFile.WriteString(result + "\n")
	if err != nil {
		log.Println("Error writing FTP result to output file:", err)
	}
}

func writeResultPlesk(outputFile *os.File, result string) {
	_, err := outputFile.WriteString(result + "\n")
	if err != nil {
		log.Println("Error writing FTP result to output file:", err)
	}
}

func writeResultWP(outputFile *os.File, result string) {
	_, err := outputFile.WriteString(result + "\n")
	if err != nil {
		log.Println("Error writing result to output file:", err)
	}
}

func writeResultWHM(outputFile *os.File, result string) {
	_, err := outputFile.WriteString(result + "\n")
	if err != nil {
		log.Println("Error writing result to output file:", err)
	}
}

func writeResultCP(outputFile *os.File, result string) {
	_, err := outputFile.WriteString(result + "\n")
	if err != nil {
		log.Println("Error writing result to output file:", err)
	}
}

func writeResultJoomla(outputFile *os.File, result string) {
	_, err := outputFile.WriteString(result + "\n")
	if err != nil {
		log.Println("Error writing result to output file:", err)
	}
}

func writeResultOjs(outputFile *os.File, result string) {
	_, err := outputFile.WriteString(result + "\n")
	if err != nil {
		log.Println("Error writing result to output file:", err)
	}
}

func writeResultGeoserver(outputFile *os.File, result string) {
	_, err := outputFile.WriteString(result + "\n")
	if err != nil {
		log.Println("Error writing result to output file:", err)
	}
}

func writeResultEvoPanel(outputFile *os.File, result string) {
	_, err := outputFile.WriteString(result + "\n")
	if err != nil {
		log.Println("Error writing result to output file:", err)
	}
}

func LogExtractor(wg *sync.WaitGroup, mutex *sync.Mutex, eName string) {
	defer wg.Done()

	file, err := os.Open("list/" + eName)
	if err != nil {
		log.Println(err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	cpanelFile, err := os.OpenFile("result/cpanel.txt", os.O_APPEND|os.O_WRONLY|os.O_CREATE, 0600)
	if err != nil {
		log.Fatal("Error creating Cpanel output file:", err)
	}
	defer cpanelFile.Close()

	ftpFile, err := os.OpenFile("result/ftp.txt", os.O_APPEND|os.O_WRONLY|os.O_CREATE, 0600)
	if err != nil {
		log.Fatal("Error creating FTP output file:", err)
	}
	defer ftpFile.Close()

	whmFile, err := os.OpenFile("result/whm.txt", os.O_APPEND|os.O_WRONLY|os.O_CREATE, 0600)
	if err != nil {
		log.Fatal("Error creating WHM output file:", err)
	}
	defer whmFile.Close()

	wordpressFile, err := os.OpenFile("result/wp.txt", os.O_APPEND|os.O_WRONLY|os.O_CREATE, 0600)
	if err != nil {
		log.Fatal("Error creating WordPress output file:", err)
	}
	defer wordpressFile.Close()

	joomlaFile, err := os.OpenFile("result/joomla.txt", os.O_APPEND|os.O_WRONLY|os.O_CREATE, 0600)
	if err != nil {
		log.Fatal("Error creating WordPress output file:", err)
	}
	defer joomlaFile.Close()

	drupalFile, err := os.OpenFile("result/drupal.txt", os.O_APPEND|os.O_WRONLY|os.O_CREATE, 0600)
	if err != nil {
		log.Fatal("Error creating Drupal output file:", err)
	}
	defer drupalFile.Close()

	phpmyadminFile, err := os.OpenFile("result/phpmyadmin.txt", os.O_APPEND|os.O_WRONLY|os.O_CREATE, 0600)
	if err != nil {
		log.Fatal("Error creating WordPress output file:", err)
	}
	defer phpmyadminFile.Close()

	prestaFile, err := os.OpenFile("result/prestashop.txt", os.O_APPEND|os.O_WRONLY|os.O_CREATE, 0600)
	if err != nil {
		log.Fatal("Error creating WordPress output file:", err)
	}
	defer prestaFile.Close()

	moodleFile, err := os.OpenFile("result/moodle.txt", os.O_APPEND|os.O_WRONLY|os.O_CREATE, 0600)
	if err != nil {
		log.Fatal("Error creating WordPress output file:", err)
	}
	defer moodleFile.Close()

	konohaFile, err := os.OpenFile("result/konoha.txt", os.O_APPEND|os.O_WRONLY|os.O_CREATE, 0600)
	if err != nil {
		log.Fatal("Error creating WordPress output file:", err)
	}
	defer konohaFile.Close()

	magentoFile, err := os.OpenFile("result/magento.txt", os.O_APPEND|os.O_WRONLY|os.O_CREATE, 0600)
	if err != nil {
		log.Fatal("Error creating WordPress output file:", err)
	}
	defer magentoFile.Close()

	owncloudFile, err := os.OpenFile("result/owncloud.txt", os.O_APPEND|os.O_WRONLY|os.O_CREATE, 0600)
	if err != nil {
		log.Fatal("Error creating WordPress output file:", err)
	}
	defer owncloudFile.Close()

	pleskFile, err := os.OpenFile("result/plesk.txt", os.O_APPEND|os.O_WRONLY|os.O_CREATE, 0600)
	if err != nil {
		log.Fatal("Error creating WordPress output file:", err)
	}
	defer pleskFile.Close()

	geoserverFile, err := os.OpenFile("result/geoserver.txt", os.O_APPEND|os.O_WRONLY|os.O_CREATE, 0600)
	if err != nil {
		log.Fatal("Error creating WordPress output file:", err)
	}
	defer geoserverFile.Close()

	ojsFile, err := os.OpenFile("result/ojs.txt", os.O_APPEND|os.O_WRONLY|os.O_CREATE, 0600)
	if err != nil {
		log.Fatal("Error creating output file:", err)
	}
	defer ojsFile.Close()

	evoFile, err := os.OpenFile("result/evopanel.txt", os.O_APPEND|os.O_WRONLY|os.O_CREATE, 0600)
	if err != nil {
		log.Fatal("Error creating output file:", err)
	}
	defer evoFile.Close()

	for scanner.Scan() {
		line := scanner.Text()
		This(func() {
			mutex.Lock()
			defer mutex.Unlock()

			if strings.Contains(line, "/phpmyadmin/") {
				if len(strings.Split(line, ":")) == 3 {
					parts := strings.Split(line, ":")
					urls := "https://" + strings.Split(line, "/")[0]
					formats := urls + "|" + parts[1] + "|" + parts[2]
					writeResultPhpmyadmin(phpmyadminFile, formats)
				}
			}

			if strings.Contains(line, "/evo/") {
				writeResultEvoPanel(evoFile, line)
			}

			if strings.Contains(line, "/index.php/") {
				writeResultOjs(ojsFile, line)
			}

			if strings.Contains(line, "geoserver") {
				writeResultGeoserver(geoserverFile, line)
			}

			if strings.Contains(line, "/login/index.php") {
				if len(strings.Split(line, ":")) == 3 {
					lines := strings.ReplaceAll(line, " ", ":")
					parts := strings.Split(lines, ":")

					if strings.Contains(parts[0], "http") {
						formats := "https:" + parts[1] + "|" + parts[2] + "|" + parts[3]
						writeResultMoodle(moodleFile, formats)
					} else {
						formats := "https://" + parts[0] + "|" + parts[1] + "|" + parts[2]
						writeResultMoodle(moodleFile, formats)
					}
				} else if len(strings.Split(line, ":")) == 4 {
					parts := strings.Split(line, ":")
					if strings.Contains(parts[0], "http") {
						formats := "https:" + parts[1] + "|" + parts[2] + "|" + parts[3]
						writeResultMoodle(moodleFile, formats)
					} else {
						formats := "https:" + parts[3] + "|" + parts[0] + "|" + parts[1]
						writeResultMoodle(moodleFile, formats)

					}
				}
			}

			if strings.Contains(line, ".id/") {
				writeResultKonoha(konohaFile, line)
			}

			if strings.Contains(line, "/owncloud/") {
				if len(strings.Split(line, ":")) == 3 {
					lines := strings.ReplaceAll(line, " ", ":")
					parts := strings.Split(lines, ":")

					if strings.Contains(parts[0], "http") {
						formats := "https:" + parts[1] + "|" + parts[2] + "|" + parts[3]
						writeResultOwncloud(owncloudFile, formats)
					} else {
						formats := "https://" + parts[0] + "|" + parts[1] + "|" + parts[2]
						writeResultOwncloud(owncloudFile, formats)
					}
				} else if len(strings.Split(line, ":")) == 4 {
					parts := strings.Split(line, ":")
					if strings.Contains(parts[0], "http") {
						formats := "https:" + parts[1] + "|" + parts[2] + "|" + parts[3]
						writeResultOwncloud(owncloudFile, formats)
					} else {
						formats := "https:" + parts[3] + "|" + parts[0] + "|" + parts[1]
						writeResultOwncloud(owncloudFile, formats)
					}
				}
			}

			if strings.Contains(line, "login_up.php") {
				parts := strings.Split(line, ":")

				if len(strings.Split(line, ":")) == 5 {

					if strings.Contains(parts[0], "http") {
						formats := "https:" + parts[1] + ":8443/login_up.php|" + parts[3] + "|" + parts[4]
						writeResultPlesk(pleskFile, formats)
					} else {
						formats := "https://" + parts[0] + ":8443/login_up.php|" + parts[2] + "|" + parts[3]
						writeResultPlesk(pleskFile, formats)
					}
				} else if len(strings.Split(line, ":")) == 4 {
					if strings.Contains(parts[0], "http") {
						formats := "https:" + parts[1] + "|" + parts[2] + "|" + parts[3]

						if strings.Contains(formats, ":8443") {
							writeResultPlesk(pleskFile, formats)
						} else {
							output := strings.Replace(formats, " 8443", ":8443", -1)
							writeResultPlesk(pleskFile, output)
						}
					} else {
						formats := "https://" + parts[0] + "|" + parts[2] + "|" + parts[3]

						if strings.Contains(formats, ":8443") {
							writeResultPlesk(pleskFile, formats)
						} else {
							output := strings.Replace(formats, " 8443", ":8443", -1)
							writeResultPlesk(pleskFile, output)
						}
					}
				}
			}

			if strings.Contains(line, "/admin/") {
				if len(strings.Split(line, ":")) == 3 {
					lines := strings.ReplaceAll(line, " ", ":")
					parts := strings.Split(lines, ":")

					if strings.Contains(parts[0], "http") {
						formats := "https:" + parts[1] + "|" + parts[2] + "|" + parts[3]
						writeResultMagento(magentoFile, formats)
					} else {
						formats := "https://" + parts[0] + "|" + parts[1] + "|" + parts[2]
						writeResultMagento(magentoFile, formats)
					}
				} else if len(strings.Split(line, ":")) == 4 {
					parts := strings.Split(line, ":")
					if strings.Contains(parts[0], "http") {
						formats := "https:" + parts[1] + "|" + parts[2] + "|" + parts[3]
						writeResultMagento(magentoFile, formats)
					} else {
						formats := "https:" + parts[3] + "|" + parts[0] + "|" + parts[1]
						writeResultMagento(magentoFile, formats)
					}
				}
			}

			if strings.Contains(line, "/user/login:") {
				url := strings.Split(line, ":")[0] + ":" + strings.Split(line, ":")[1]
				user := strings.Split(line, ":")[2]
				pass := strings.Split(line, ":")[3]

				formats := url + "|" + user + "|" + pass
				writeResultDrupal(drupalFile, formats)
			}

			if strings.Contains(line, "/user/login ") {
				url := strings.Split(line, " ")[0]
				user := strings.Split(strings.Split(line, " ")[1], ":")[0]
				pass := strings.Split(strings.Split(line, " ")[1], ":")[0]

				formats := url + "|" + user + "|" + pass
				writeResultDrupal(drupalFile, formats)
			}

			// PrestaShop
			if regexp.MustCompile("/admin.*/index\\.php").MatchString(line) {
				if len(strings.Split(line, ":")) == 4 {
					if strings.HasPrefix(line, "http") {
						parts := strings.Split(line, ":")
						formats := "https:" + parts[1] + "|" + parts[2] + "|" + parts[3]
						writeResultPresta(prestaFile, formats)
					} else {
						parts := strings.Split(line, ":")
						formats := "https:" + parts[3] + "|" + parts[0] + "|" + parts[1]
						writeResultPresta(prestaFile, formats)
					}
				}
			}

			if strings.Contains(line, "/administrator/index.php") {
				if len(strings.Split(line, ":")) == 3 {
					parts := strings.Split(line, ":")
					formats := "https://" + parts[0] + "|" + parts[1] + "|" + parts[2]
					writeResultJoomla(joomlaFile, formats)
				} else {
					urls := "https" + regexp.MustCompile(`://(.*?)/administrator/index.php`).FindStringSubmatch(line)[0]
					if len(strings.Split(line, ":")) == 4 {
						username := strings.Split(line, ":")[2]
						password := strings.Split(line, ":")[3]
						formats := urls + "|" + username + "|" + password
						writeResultJoomla(joomlaFile, formats)
					} else if len(strings.Split(line, ":")) == 5 {
						username := strings.Split(line, ":")[3]
						password := strings.Split(line, ":")[4]
						formats := urls + "|" + username + "|" + password
						writeResultJoomla(joomlaFile, formats)
					}
				}
			}

			// Cpanel
			if strings.Contains(line, ":2083") {
				if strings.Contains(line, "://") {
					urls := "https" + regexp.MustCompile(`://(.*?):2083`).FindStringSubmatch(line)[0]
					username := strings.Split(line, ":")[3]
					password := strings.Split(line, ":")[4]
					formats := urls + "|" + username + "|" + password
					writeResultCP(cpanelFile, formats)
				} else {
					pattern := `^(.*?):\d+/.*?:(.*?):(.*)$`
					re := regexp.MustCompile(pattern)
					matches := re.FindStringSubmatch(line)
					if len(matches) == 4 {
						result := fmt.Sprintf("https://%s:2083|%s|%s", matches[1], matches[2], matches[3])
						writeResultCP(cpanelFile, result)
					}
				}
			}
			if strings.Contains(line, ":2082") {
				if strings.Contains(line, "://") {
					urls := "https" + regexp.MustCompile(`://(.*?):2082`).FindStringSubmatch(line)[0]
					username := strings.Split(line, ":")[3]
					password := strings.Split(line, ":")[4]
					formats := urls + "|" + username + "|" + password
					writeResultCP(cpanelFile, formats)
				} else {
					pattern := `^(.*?):\d+/.*?:(.*?):(.*)$`
					re := regexp.MustCompile(pattern)
					matches := re.FindStringSubmatch(line)
					if len(matches) == 4 {
						result := fmt.Sprintf("https://%s:2082|%s|%s", matches[1], matches[2], matches[3])
						writeResultCP(cpanelFile, result)
					}
				}
			}

			// FTP
			if strings.Contains(line, "ftp.") {
				if strings.Contains(line, "ftp://") {
					pattern := `^ftp://([^:/]+)/:([^:]+):([^@]+)$`
					re := regexp.MustCompile(pattern)
					matches := re.FindStringSubmatch(line)

					if len(matches) == 4 {
						result := fmt.Sprintf("ftp://%s|%s|%s", matches[1], matches[2], matches[3])
						writeResultFTP(ftpFile, result)
					}
				} else {
					if len(strings.Split(line, ":")) == 3 {
						if strings.Contains(line, "/:") {
							formatted := strings.Replace(line, "/:", "|", 1)
							formatted = strings.Replace(formatted, ":", "|", 1)
							writeResultFTP(ftpFile, formatted)
						}
					}
				}
			}

			// WHM
			if strings.Contains(line, ":2087") {
				if strings.Contains(line, "://") {
					urls := "https" + regexp.MustCompile(`://(.*?):2087`).FindStringSubmatch(line)[0]
					username := strings.Split(line, ":")[3]
					password := strings.Split(line, ":")[4]
					formats := urls + "|" + username + "|" + password
					writeResultWHM(whmFile, formats)
				} else {
					pattern := `^(.*?):\d+/.*?:(.*?):(.*)$`
					re := regexp.MustCompile(pattern)
					matches := re.FindStringSubmatch(line)
					if len(matches) == 4 {
						result := fmt.Sprintf("https://%s:2087|%s|%s", matches[1], matches[2], matches[3])
						writeResultWHM(whmFile, result)
					}
				}
			}
			if strings.Contains(line, ":2086") {
				if strings.Contains(line, "://") {
					urls := "https" + regexp.MustCompile(`://(.*?):2086`).FindStringSubmatch(line)[0]
					username := strings.Split(line, ":")[3]
					password := strings.Split(line, ":")[4]
					formats := urls + "|" + username + "|" + password
					writeResultWHM(whmFile, formats)
				} else {
					pattern := `^(.*?):\d+/.*?:(.*?):(.*)$`
					re := regexp.MustCompile(pattern)
					matches := re.FindStringSubmatch(line)
					if len(matches) == 4 {
						result := fmt.Sprintf("https://%s:2086|%s|%s", matches[1], matches[2], matches[3])
						writeResultWHM(whmFile, result)
					}
				}
			}

			if strings.Contains(line, "wp-login.php") {
				if len(strings.Split(line, ":")) == 3 {
					parts := strings.Split(line, ":")
					formats := "https://" + parts[0] + "#" + parts[1] + "@" + parts[2]
					writeResultWP(wordpressFile, formats)
				} else {
					pattern := `^(https://[^/]+/wp-login.php):([^:]+):(.+)$`
					re := regexp.MustCompile(pattern)
					matches := re.FindStringSubmatch(line)

					if len(matches) == 4 {
						result := fmt.Sprintf("%s#%s@%s", matches[1], matches[2], matches[3])
						writeResultWP(wordpressFile, result)
					}
				}
			}
		}).Catch(func(E) {
			return
		})
	}

	if err := scanner.Err(); err != nil {
		log.Println(err)
	}
}

func main() {
	var wg sync.WaitGroup
	var mutex sync.Mutex

	entries, err := os.ReadDir("./list")
	if err != nil {
		log.Fatal(err)
	}

	for _, e := range entries {
		wg.Add(1)
		go LogExtractor(&wg, &mutex, e.Name())
	}

	wg.Wait()
	fmt.Println("DONE")
	os.Exit(0)
}
