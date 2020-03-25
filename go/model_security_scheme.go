/*
 * Onshape REST API
 *
 * The Onshape REST API consumed by all clients.
 *
 * API version: 1.111
 * Contact: api-support@onshape.zendesk.com
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package openapi
// SecurityScheme struct for SecurityScheme
type SecurityScheme struct {
	BearerFormat string `json:"bearerFormat,omitempty"`
	Description string `json:"description,omitempty"`
	Extensions map[string]map[string]interface{} `json:"extensions,omitempty"`
	Flows OAuthFlows `json:"flows,omitempty"`
	Getref string `json:"get$ref,omitempty"`
	In string `json:"in,omitempty"`
	Name string `json:"name,omitempty"`
	OpenIdConnectUrl string `json:"openIdConnectUrl,omitempty"`
	Scheme string `json:"scheme,omitempty"`
	Type string `json:"type,omitempty"`
}
